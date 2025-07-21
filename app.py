# -*- coding: utf-8 -*-

"""
Project Odyssey: AI Safety Agent - Proof-of-Concept Script
===========================================================

This script simulates the core logic of the Odyssey system.
It demonstrates how the AI agent processes multimodal events (vision, audio),
fuses them to understand context, and escalates threat levels to prevent accidents.

- Author: Hyun-woo Kim (Team Kim Hyun-woo)
- For: 2025 AI Champion Challenge
"""

import time
import datetime
import random

# ANSI escape codes for colored terminal output
class Colors:
    RESET = '\033[0m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'

class OdysseyAgent:
    """Simulates the Odyssey AI Safety Agent."""

    def __init__(self):
        self.threat_level = 'LOW'
        self.knowledge_base = {} # Stores facts derived from events
        self.log("INFO", "Odyssey Agent Initialized. System is nominal.")

    def log(self, level, message):
        """Prints a formatted and colored log message."""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        color = ''
        if level == 'INFO':
            color = Colors.BLUE
        elif level == 'WARN':
            color = Colors.YELLOW
        elif level == 'CRITICAL':
            color = Colors.RED + Colors.BOLD
        
        print(f"{timestamp} | {color}[{level.ljust(8)}] {message}{Colors.RESET}")

    def process_event(self, event):
        """Processes a single event from a modality."""
        modality = event['modality'].upper()
        data = event['data']
        self.log("INFO", f"[{modality}] Event received: {data['description']}")

        # --- Single-modality analysis ---
        if modality == 'VISION':
            if 'unsafe_behavior' in data and data['unsafe_behavior'] == 'no_helmet':
                self.log("WARN", "Vision module detected a worker without a safety helmet.")
                self.knowledge_base['unprotected_worker'] = True
                self.threat_level = 'MEDIUM'

        elif modality == 'AUDIO':
            if 'abnormal_sound' in data and data['abnormal_sound'] == 'high_freq_squeal':
                self.log("WARN", "Audio module detected abnormal high-frequency noise from machinery.")
                self.knowledge_base['faulty_machine'] = True
                self.threat_level = 'MEDIUM'
        
        # --- Multimodal Fusion Analysis ---
        self.analyze_situation()

    def analyze_situation(self):
        """
        The core of the agent. Fuses knowledge from different modalities 
        to understand the complete context and identify critical threats.
        """
        # This is the "Aha!" moment of the project.
        # Individually, they are just MEDIUM threats. Together, they are CRITICAL.
        if self.knowledge_base.get('unprotected_worker') and self.knowledge_base.get('faulty_machine'):
            if self.threat_level != 'CRITICAL':
                self.threat_level = 'CRITICAL'
                self.log("CRITICAL", "MULTIMODAL FUSION ALERT!")
                self.log("CRITICAL", "An unprotected worker is near potentially malfunctioning equipment.")
                self.log("CRITICAL", "Immediate intervention required. Escalating to highest alert level.")
                # In a real system, this would trigger alarms, send notifications, etc.

    def generate_final_report(self):
        """Generates a summary report at the end of the scenario."""
        print("\n" + "="*60)
        print("          Project Odyssey: Scenario End Report")
        print("="*60)
        print(f"  - Final Threat Level: {self.threat_level}")
        print("  - Key Findings:")
        if self.knowledge_base.get('unprotected_worker'):
            print("    - [VISION] Unsafe behavior detected (No Helmet).")
        if self.knowledge_base.get('faulty_machine'):
            print("    - [AUDIO] Equipment anomaly detected (Abnormal Noise).")
        if self.threat_level == 'CRITICAL':
            print("    - [FUSION] Critical risk identified by combining vision and audio data.")
        print("="*60)
        print("Simulation complete.\n")


def run_simulation():
    """Defines and runs a predefined scenario."""

    # This scenario simulates the events from our interactive demo
    scenario_events = [
        {'modality': 'vision', 'data': {'description': 'Worker enters Zone 3B'}},
        {'modality': 'vision', 'data': {'description': 'Checking for safety gear...', 'unsafe_behavior': 'no_helmet'}},
        {'modality': 'audio', 'data': {'description': 'Monitoring machine noise...'}},
        {'modality': 'audio', 'data': {'description': 'High-frequency sound detected!', 'abnormal_sound': 'high_freq_squeal'}},
        {'modality': 'vision', 'data': {'description': 'Worker is now in close proximity to the machine.'}},
    ]

    agent = OdysseyAgent()
    time.sleep(1)

    print("\n" + "-"*60)
    print("      Starting Industrial Safety Scenario Simulation...")
    print("-"*60 + "\n")
    time.sleep(2)

    for event in scenario_events:
        agent.process_event(event)
        time.sleep(random.uniform(2, 3)) # Simulate time passing between events
    
    agent.generate_final_report()


if __name__ == "__main__":
    run_simulation()
