**Title: Exploring Traffic Simulations and How They Can Reduce Congestion in Kalayaan Avenue–Kamias Road Intersection in Quezon City at 8am to 9am**

**Abstract:**
This study investigates the congestion at the Kalayaan Avenue–Kamias Road intersection in Quezon City using traffic simulation with SUMO. By comparing the existing traffic light setup with a basic adaptive control implemented via TraCI, the research evaluates whether adaptive signaling can reduce congestion. Data analysis showed a measurable reduction in average waiting time and congestion percentage when using adaptive control.

**1. Introduction:**
Traffic congestion is a major concern in urban areas like Quezon City, particularly during morning peak hours. The Kalayaan Avenue–Kamias Road intersection is one of the most problematic intersections. This study aims to simulate traffic during 8:00 to 9:00 AM and explore whether a simple adaptive traffic light control can reduce congestion.

**2. Methodology:**

2.1 Map and Network Preparation:

* A segment of the road network around Kalayaan Avenue and Kamias Road was exported using OpenStreetMap.
* The exported OSM file was converted to a SUMO network using netconvert.

2.2 Base Simulation:

* A route file (.rou.xml) was created to simulate traffic flow.
* A fixed-time traffic light logic was defined in the SUMO network.
* Simulation was run and the tripinfo output was recorded.

2.3 Data Extraction and Cleaning:

* tripinfo.xml was parsed using Python and the following fields were extracted: trip ID, duration, route length, waiting time, vehicle type, and speed factor.
* Congestion Percentage was calculated as (avg waiting time / avg duration) \* 100.
* Summary statistics and plots were generated.

2.4 Adaptive Simulation with TraCI:

* A Python script using TraCI API was created.
* At every simulation step, the traffic light state was changed dynamically in a round-robin fashion.
* tripinfo.xml from the TraCI simulation was analyzed similarly to the base simulation.

**3. Results and Analysis:**

| Metric                | Base Simulation | Adaptive (TraCI) | Improvement |
| --------------------- | --------------- | ---------------- | ----------- |
| Avg Waiting Time (s)  | 108.5           | 14.15            | -Z.ZZ%      |
| Avg Duration (s)      | 161.00          | 63.3             |             |
| Congestion Percentage | 67.60%          | 22.37%           | -66.91%      |



Graphs:
![image](https://github.com/user-attachments/assets/e7b42b47-4846-45ce-b200-41b972dc1e95)
![image](https://github.com/user-attachments/assets/a62f6ce1-b32f-46a3-9065-05944a6e7a7c)
![image](https://github.com/user-attachments/assets/81c62936-5b62-422d-b7e8-91cb6c9fcd49)



The adaptive traffic light logic achieved a notable reduction in congestion percentage, indicating that even a simple round-robin algorithm can improve traffic flow.

**4. Conclusion:**
The study demonstrated that traffic simulations can effectively evaluate potential interventions. Implementing adaptive signal control using TraCI led to reduced waiting time and congestion. While basic, the strategy shows promise and can be refined further.

**5. Limitations and Future Work:**

* Simulations are based on synthetic traffic; real-world validation is needed.
* Only a basic round-robin logic was used.
* Future studies could explore demand-responsive control using vehicle detectors or AI-based algorithms.

**Appendices:**

* Sample SUMO configuration.
* Sample output CSV.
* Python scripts used for data extraction and control.

**References:**

* SUMO Documentation
* OpenStreetMap
* TraCI API Reference
