from django.shortcuts import redirect, render
from .preprocessing import *


from datetime import datetime, timedelta

def main_dashboard(request):
    # Load the DataFrame from CSV
    df = pd.read_csv('media/df/saga_instace_file.csv')

    # Process data to calculate required statistics
    total_executions = len(df)
    print(df.status.value_counts().index,flush=True)
    completed_successfully = df[df['status'] == 'COMPLETED']
    completed_with_error = df[df['status'] == 'FAILED']
    being_completed = df[df['status'] == 'PENDING' | df['status'] == 'IN_PROGRESS']  # Assuming 'PENDING'  status also means being completed
    compensated = df[df['status'] == 'COMPENSATED']
    # Calculating numbers and percentages
    num_completed_successfully = len(completed_successfully)
    perc_completed_successfully = (num_completed_successfully / total_executions) * 100
    num_completed_with_error = len(completed_with_error)
    perc_completed_with_error = (num_completed_with_error / total_executions) * 100
    num_being_completed = len(being_completed)
    perc_being_completed = (num_being_completed / total_executions) * 100
    num_compensated = len(compensated)  # Number of compensated executions
    perc_compensated = (num_compensated / total_executions) * 100  # Percentage of compensated executions

    # Preparing data for processes requiring review and recent executions
    review_processes = df[df['status'] == 'REVIEW']  # Assuming 'REVIEW' status requires review
    df['createdAt_$date'] = pd.to_datetime(df['createdAt_$date']).dt.tz_localize(None)
    one_hour_ago = datetime.now() - timedelta(hours=1)
    recent_executions = df[df['createdAt_$date'] > one_hour_ago]

    # Passing data to the template
    context = {
        'total_executions': total_executions,
        'num_completed_successfully': num_completed_successfully,
        'perc_completed_successfully': perc_completed_successfully,
        'num_completed_with_error': num_completed_with_error,
        'perc_completed_with_error': perc_completed_with_error,
        'num_being_completed': num_being_completed,
        'perc_being_completed': perc_being_completed,
        'num_compensated': num_compensated,  # Add to context
        'perc_compensated': perc_compensated,  # Add to context
        'review_processes': review_processes.to_html(),  # Convert DataFrame to HTML table
        'recent_executions': recent_executions.to_html(),  # Convert DataFrame to HTML table
    }
    return render(request, 'dash_board/main_dashboard.html', context)


def home_page(request):
    return render (request,'dash_board/base.html')



from django.core.files.storage import FileSystemStorage
from .models import VivebFile
from .file_processing import save_files, load_files

def file_upload(request):
    if request.method == 'POST':
        uploaded_files = {
            'saga': request.FILES.get('saga_file'),
            'saga_instance': request.FILES.get('saga_instance_file'),
            'saga_log': request.FILES.get('saga_log_file')
        }
        save_files(uploaded_files)
        return redirect('file_upload')  # Redirect to a success page or the same page

    saga_files = load_files()
    return render(request, 'dash_board/file_upload.html', {'saga_files': saga_files})
       