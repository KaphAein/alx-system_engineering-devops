For every additional element, why you are adding it:

Each additional element in the infrastructure serves a specific purpose to enhance functionality, performance, or security. For example:
Load balancer: To distribute incoming traffic across multiple servers for improved scalability, availability, and performance.
Firewall: To control and filter incoming and outgoing network traffic to protect the infrastructure from unauthorized access, malware, and other security threats.
HTTPS: To encrypt data transmitted between clients and servers, ensuring confidentiality, integrity, and authenticity of the communication.
Monitoring: To track the health, performance, and availability of the infrastructure components and identify issues proactively.
Additional servers: To handle increased workload, improve fault tolerance, and provide redundancy.
What are firewalls for:

Firewalls are network security devices or software that monitor and control incoming and outgoing network traffic based on predetermined security rules. They act as a barrier between a trusted internal network and untrusted external networks (such as the internet), filtering traffic to prevent unauthorized access, data breaches, and other malicious activities.
Why is the traffic served over HTTPS:

Traffic is served over HTTPS to encrypt data transmitted between clients and servers, providing confidentiality, integrity, and authenticity of the communication. HTTPS protects sensitive information such as login credentials, personal data, and financial transactions from eavesdropping, tampering, and man-in-the-middle attacks.
What monitoring is used for:

Monitoring is used to track the performance, health, and availability of the infrastructure components and applications. It helps identify issues, troubleshoot problems, optimize resource utilization, and ensure service reliability. Monitoring allows for proactive management, capacity planning, and continuous improvement of the infrastructure.
How the monitoring tool is collecting data:

Monitoring tools collect data through various methods such as:
Polling: Regularly querying system metrics, logs, and performance counters from monitored devices and servers.
Agents: Installing lightweight software agents on monitored systems to gather real-time data and transmit it to the monitoring server.
Event-based triggers: Reacting to predefined events or thresholds and triggering alerts or actions based on the monitored conditions.
APIs: Integrating with APIs provided by applications, cloud services, or infrastructure components to retrieve metrics and status information.
Explain what to do if you want to monitor your web server QPS:

To monitor the Query Per Second (QPS) on a web server, you can:
Use monitoring tools such as Prometheus, Grafana, or Nagios to collect and visualize QPS metrics.
Configure the monitoring tool to capture HTTP request rates or server-side processing rates.
Monitor server logs for incoming request counts over time.
Set up alerts or notifications to trigger when QPS exceeds predefined thresholds, indicating potential performance issues or traffic spikes.
Why terminating SSL at the load balancer level is an issue:

Terminating SSL (decrypting HTTPS traffic) at the load balancer level can be an issue because it exposes the decrypted data within the internal network, potentially compromising data security and violating compliance requirements. It also adds overhead to the load balancer, impacting its performance and scalability.
Why having only one MySQL server capable of accepting writes is an issue:

Having only one MySQL server capable of accepting writes creates a single point of failure (SPOF) for write operations. If the primary MySQL server fails, write operations will be disrupted, leading to data inconsistency and service downtime. It also limits scalability and fault tolerance, as the system cannot distribute write traffic across multiple servers.
Why having servers with all the same components (database, web server, and application server) might be a problem:

Having servers with identical components may lead to homogeneity, making the infrastructure vulnerable to widespread failures, security vulnerabilities, or software bugs. It also limits flexibility and agility in adapting to diverse workloads, evolving requirements, or technological advancements. Introducing diversity in the infrastructure architecture can enhance resilience, mitigate risks, and optimize resource utilization.