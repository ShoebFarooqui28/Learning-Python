from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto = True, margin = 15)
pdf.add_page()
pdf.set_font("Arial", size = 12)

content = """
NIOS Physics Study Plan: 8-Month Schedule

General Approach
- Study Hours per Day: 3-4 hours on weekdays, 5-6 hours on weekends.
- Focus Areas:
  - Theory (60%): Conceptual clarity from textbooks and notes.
  - Numerical Problems (30%): Solve related questions.
  - Revision (10%): Daily recap of what you learned.

Month 1: Module-I (Motion, Force, and Energy)
Goal: Cover lessons 1 to 4 thoroughly.
Week 1: Lesson 1: Units, Dimensions, and Vectors
- Learn dimensional analysis, vector addition, and resolution. Solve 10 numerical problems.
- Time Allocation: 1.5 hrs theory, 1.5 hrs practice daily

Week 1: Lesson 2: Motion in a Straight Line
- Study kinematics equations and graphs. Practice 15 numerical problems.

Week 2: Lesson 3: Laws of Motion
- Learn Newton's laws and free-body diagrams. Solve 20 numerical problems.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 3: Lesson 4: Motion in a Plane
- Study projectile motion and relative velocity. Practice vector-based problems.
- Time Allocation: 1.5 hrs theory, 1.5 hrs practice daily

Week 4: Revision of Lessons 1-4
- Solve mixed questions from all 4 topics. Attempt a small self-test.
- Time Allocation: 2 hrs revision, 2 hrs testing

Month 2: Complete Module-I
Goal: Lessons 5 to 7 (Gravitation, Work-Energy-Power, Motion of a Rigid Body).

Week 1: Lesson 5: Gravitation
- Study laws of gravitation, orbital velocity, and escape speed. Solve 15 numerical problems.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 2: Lesson 6: Work, Energy, and Power
- Understand work-energy theorem, conservative forces, and power.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 3: Lesson 7: Motion of a Rigid Body
- Study torque, moment of inertia, and angular momentum.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 4: Revision of Module-I
- Revise Lessons 1-7. Solve mixed numerical problems.
- Time Allocation: 3 hrs practice, 1 hr recap daily

Month 3: Module-II and Start Module-III
Goal: Complete mechanics of solids and fluids, start thermal physics.

Week 1: Lesson 8: Elastic Properties of Solids
- Study stress, strain, Young’s modulus. Solve 10 numerical problems.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 2: Lesson 9: Properties of Fluids
- Understand Bernoulli’s equation, viscosity, and surface tension.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 3: Lesson 10: Kinetic Theory of Gases
- Learn gas laws and molecular speeds. Solve related problems.
- Time Allocation: 1.5 hrs theory, 1.5 hrs practice daily

Week 4: Lesson 11: Thermodynamics
- Study laws of thermodynamics, heat engines. Practice 15 numerical problems.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Month 4: Module-IV and Continue Module-V
Goal: Oscillations, waves, and basics of electricity.

Week 1: Lesson 13: Simple Harmonic Motion
- Study oscillation equations and energy. Solve problems on pendulums.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 2: Lesson 14: Wave Phenomena
- Learn wave equations, interference, and Doppler effect.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Week 3: Lesson 15: Electric Charge and Field
- Study Coulomb’s law, field lines, and Gauss’s law.
- Time Allocation: 1.5 hrs theory, 1.5 hrs practice daily

Week 4: Lesson 16: Electric Potential
- Understand potential, capacitance, and energy storage.
- Time Allocation: 1.5 hrs theory, 1.5 hrs practice daily

Months 5-6: Modules-VI, VII, VIII
Goal: Cover optics, atomic physics, and semiconductors.

Month 5: Lessons 20-23: Optics
- Study reflection, refraction, interference, and optical instruments.
- Time Allocation: 2 hrs theory, 2 hrs practice daily

Lessons 24-25: Atoms and Nuclei
- Study atomic models, dual nature, and radiation.

Month 6: Lessons 28-30: Semiconductors
- Learn diode circuits, communication systems, and applications. Solve 10 numerical problems daily.
- Time Allocation: 1.5 hrs theory, 1.5 hrs practice daily

Months 7-8: Revision and Practice
Goal: Strengthen weak areas and simulate exam conditions.

Week 1: Revise Modules I-III
- Focus on key concepts, solve past papers.
- Time Allocation: 3 hrs daily

Week 2: Revise Modules IV-V
- Practice numerical questions on electricity and magnetism.
- Time Allocation: 3 hrs daily

Week 3: Revise Modules VI-VIII
- Focus on optics, nuclear physics, and semiconductors.
- Time Allocation: 3 hrs daily

Week 4: Full-Length Mock Tests
- Attempt timed tests and review mistakes.
- Time Allocation: 5 hrs per test day

Tips for Success
- Daily Recap: Spend 15-30 minutes reviewing what you studied.
- Use Visual Aids: Draw diagrams for optics, SHM, and waves.
- Focus on PE Lessons: Pay extra attention to the lessons marked for Public Examinations (PE).
- Stay Consistent: Follow the schedule strictly to avoid falling behind.
- Track Progress: Weekly self-tests will help gauge understanding.
"""

content = content.replace("‘", "'").replace("’", "'").replace("–", "-").replace("—", "-")
pdf.multi_cell(0, 10, content)

pdf.output("NIOS-Prep.pdf")