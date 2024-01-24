from django.shortcuts import redirect, render
from .preprocessing import *
import pandas as pd

from datetime import datetime, timedelta
from .main_dashboad_processor import MainDashboard


main_dashboard_processor= MainDashboard()


def main_dashboard(request):
    context = main_dashboard_processor.get_process_execution_stats()  # Common context
    context['status_options'] = main_dashboard_processor.get_status_options()

    if request.method == 'POST':
        try:
            # Parsing selected values from the dropdown
            selected_statuses = request.POST.getlist('statuses')

            # Parsing values from the date-time pickers
            start_time_str = request.POST.get('start_time')
            end_time_str = request.POST.get('end_time')

            # Convert time strings to datetime objects, handling invalid formats
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M') if start_time_str else None
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M') if end_time_str else None

            # Filter data and convert to HTML table
            processes = main_dashboard_processor.filter_dataframe(status=selected_statuses, time_beg=start_time, time_end=end_time)
            processes = processes.to_html() if processes is not None else 'No data available'

            context['processes'] = processes

        except ValueError as e:
            # Handle specific error (e.g., date parsing error)
            context['error'] = f"Invalid input: {e}"
        except Exception as e:
            # Handle any other unforeseen errors
            context['error'] = f"An error occurred: {e}"

    # Render the template with context
    return render(request, 'dash_board/main_dashboard.html', context)


def home_page(request):
    return render (request,'dash_board/base.html')



from django.core.files.storage import FileSystemStorage
from .models import VivebFile
from .file_processing import save_files, load_files





from .saga import parse_saga_file
from .saga_instance import parse_saga_instance_file
from .saga_log import parse_saga_instance_log_file
def save_to_df(uploaded_files):
    try:
        for file_type, file in uploaded_files.items():
            if file is not None:
                if file_type == 'saga':
                    # Assuming parse_saga_file is your custom function for 'saga' file type
                    print("in saga",type(file),flush=True)
                    file.seek(0)
                    parse_saga_file(file.read())
                elif file_type == 'saga_instance':
                    # Using the parse_saga_instance_file function
                    file.seek(0)
                    parse_saga_instance_file(file.read())
                elif file_type == 'saga_log':
                    # Handle saga_log file or skip if not implemented
                    file.seek(0)
                    parse_saga_instance_log_file(file.read())
                else:
                    print(f"Unknown file type: {file_type}")

    except Exception as e:
        print(f"An error occurred: {e}")



def file_upload(request):
    if request.method == 'POST':
        uploaded_files = {
            'saga': request.FILES.get('saga_file'),
            'saga_instance': request.FILES.get('saga_instance_file'),
            'saga_log': request.FILES.get('saga_log_file')
        }
        #lets save the files to DB
        save_files(uploaded_files)
        #also we should convert them to a dataframe
        save_to_df(uploaded_files)
        
        return redirect('file_upload')  # Redirect to a success page or the same page

    saga_files = load_files()
    return render(request, 'dash_board/file_upload.html', {'saga_files': saga_files})
       