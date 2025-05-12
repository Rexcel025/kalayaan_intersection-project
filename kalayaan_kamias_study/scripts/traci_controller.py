import traci
import sumolib
import os
import time

def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        for tl_id in traci.trafficlight.getIDList():
            controlled_lanes = traci.trafficlight.getControlledLanes(tl_id)
            vehicles = []

            # Get all vehicles on controlled lanes
            for lane in controlled_lanes:
                vehicles += traci.lane.getLastStepVehicleIDs(lane)

            waiting_time = sum(traci.vehicle.getWaitingTime(v) for v in vehicles)

            # Example simple adaptive logic: change phase if waiting time is too high
            if waiting_time > 100:
                current_phase = traci.trafficlight.getPhase(tl_id)
                total_phases = len(traci.trafficlight.getAllProgramLogics(tl_id)[0].phases)
                next_phase = (current_phase + 1) % total_phases
                traci.trafficlight.setPhase(tl_id, next_phase)

        step += 1

    traci.close()
    print("✅ Simulation with adaptive control complete.")

if __name__ == "__main__":
    sumoBinary = "sumo"  # or "sumo-gui" for GUI version
    sumoCmd = [sumoBinary, "-c", "input/kalayaan_kamias.sumocfg", "--tripinfo-output", "output/tripinfo_traci.xml"]
    traci.start(sumoCmd)
    run()
