# Minor Project 2: Zero Trust Architecture for Enterprise Security

### Project Overview
This project demonstrates a Zero Trust security framework designed for an enterprise environment. Unlike traditional security models that trust any user inside the network, this system follows the "Never Trust, Always Verify" principle. 

This simulation was built to fulfill the requirements for my cybersecurity internship project, focusing on Identity & Access Management (IAM) and network micro-segmentation.

### Key Security Features
* **Role-Based Access Control (RBAC):** The system differentiates between "Admin" and "Guest" roles, ensuring users only access what they need.
* **MFA Simulation:** Access to the secure data tier requires a specific authentication token, simulating Multi-Factor Authentication.
* **Micro-segmentation:** The backend database logic is isolated from the front-end portal, preventing unauthorized lateral movement.

### System Architecture
The project is split into two Python-based services to simulate a segmented network:
1.  `database_system.py`  : This acts as the isolated "Secure Zone." It holds sensitive data and requires a valid token for every request.
2.  `enterprise_portal.py`: This is the "Public Zone" where users log in. It enforces the access policies before attempting to communicate with the database.



### How to Run the Simulation
1.  Ensure Python 3.13 or higher is installed.
2.  Place both `database_system.py` and `enterprise_portal.py` in the same directory.
3.  Open the Command Prompt, navigate to the folder, and run:
    python enterprise_portal.py

### Lab Results & Testing
I conducted two primary tests to verify the security effectiveness:

| Test Case               | Role    | Input    | System Response                                          |
| **Authorized Access**   | Admin   | Choice 1 | **SUCCESS:** Identity verified; sensitive data released. |
| **Unauthorized Access** | Guest   | Choice 2 | **FAILURE:** Access Denied; RBAC policy enforced.        |

During testing, the system successfully blocked a "Guest" user from accessing the project files, proving that the identity verification layer works correctly.

### Future Improvements
* **Automated Threat Detection:** Implementing a script to flag multiple failed login attempts.
* **Data Encryption:** Adding a layer of encryption for the tokens passed between scripts to prevent interception.