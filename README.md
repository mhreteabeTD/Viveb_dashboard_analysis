# Viveb Dashboard Analysis

## Project Overview
This Dockerized project creates a comprehensive dashboard for monitoring and analyzing API usage within Viveb's server environments. It aims to provide actionable insights into API performance trends, enhancing server management and operational reliability.

**Screenshots**

![image](https://github.com/user-attachments/assets/782f4e10-7959-4b09-9be7-60cef40421a7)

![image](https://github.com/user-attachments/assets/36e2aa4c-7545-459b-814b-3e985b444ac9)

![image](https://github.com/user-attachments/assets/4ca17637-0626-4b44-a567-e24551618605)





## Features
- **Data Visualization:** Leverages Matplotlib to craft dynamic visual representations of API usage statistics.
- **Data Management:** Utilizes Django for robust backend processes to track API lifecycle and manage data efficiently.
- **Performance Insights:** Offers analytics on API performance, aiding in optimization and reliability enhancements.


## Technologies Used
- Django
- Django REST Framework
- Matplotlib
- Pandas
- Docker

## Installation
To run this project using Docker, follow these steps:
1. Clone the repository:
   ```
   git clone https://github.com/mhreteabeTD/Viveb_dashboard_analysis.git
   ```
2. Navigate to the project directory:
   ```
   cd Viveb_dashboard_analysis
   ```
3. Build the Docker container:
   ```
   docker build -t viveb_dashboard .
   ```
4. Run the container:
   ```
   docker run -p 8000:8000 viveb_dashboard
   ```

## Usage
Once the Docker container is running, access the dashboard through your web browser at `http://localhost:8000` to interact with the API usage data.

## Contributing
Feel free to contribute to improving the dashboard. Fork the project, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
