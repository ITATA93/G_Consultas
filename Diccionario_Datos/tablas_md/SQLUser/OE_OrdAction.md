# SQLUser.OE_OrdAction

**Schema:** SQLUser
**Columnas:** 195
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACT_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ACT_Action | varchar |  |  | SI | Action |
| ACT_Childsub | double |  |  | NO | Childsub |
| ACT_Date | date |  |  | SI | Date |
| ACT_RowId | varchar |  |  | NO | - |
| ACT_Time | time |  |  | SI | Time |
| ACT_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| ACT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ACT_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Affected limb |
| Q02 | - |  |  | SI | Dominance |
| Q03 | - |  |  | SI | Pre-existing conditions impacting on upper limb fu... |
| Q04 | - |  |  | SI | Subluxation |
| Q05 | - |  |  | SI | Is patient able to shrug shoulders |
| Q06 | - |  |  | SI | Finger breadth (1 finger - approx 10mm) |
| Q07 | - |  |  | SI | Pain |
| Q08 | - |  |  | SI | Pain location |
| Q09 | - |  |  | SI | Oedema |
| Q10 | - |  |  | SI | Oedema location |
| Q100 | - |  |  | SI | Elbow flexion |
| Q101 | - |  |  | SI | Release |
| Q102 | - |  |  | SI | Write your name with a pen |
| Q103 | - |  |  | SI | Left |
| Q104 | - |  |  | SI | Right |
| Q105 | - |  |  | SI | Quality of movement |
| Q106 | - |  |  | SI | Shoulder forward flexion |
| Q107 | - |  |  | SI | Shoulder external rotation |
| Q108 | - |  |  | SI | Elbow extension |
| Q109 | - |  |  | SI | Grasp |
| Q11 | - |  |  | SI | Tone |
| Q110 | - |  |  | SI | In hand manipulation |
| Q111 | - |  |  | SI | Turn over paper / newspaper |
| Q112 | - |  |  | SI | Left |
| Q113 | - |  |  | SI | Right |
| Q114 | - |  |  | SI | Shoulder forward flexion |
| Q115 | - |  |  | SI | Pronation |
| Q116 | - |  |  | SI | Supination |
| Q117 | - |  |  | SI | Functional Grasps |
| Q118 | - |  |  | SI | Left |
| Q119 | - |  |  | SI | Right |
| Q12 | - |  |  | SI | Tone location |
| Q120 | - |  |  | SI | Quality of movement |
| Q121 | - |  |  | SI | Functional Grasps |
| Q122 | - |  |  | SI | Grip Strength |
| Q123 | - |  |  | SI | Co-ordination |
| Q124 | - |  |  | SI | Left |
| Q125 | - |  |  | SI | Right |
| Q126 | - |  |  | SI | Bilateral integration |
| Q127 | - |  |  | SI | (supination / pronation) |
| Q128 | - |  |  | SI | Rapid Alternating Movements (RAM) |
| Q129 | - |  |  | SI | Finger – Nose |
| Q13 | - |  |  | SI | Active Range of Motion Analysis |
| Q130 | - |  |  | SI | Opposition |
| Q131 | - |  |  | SI | Sensation hot / cold |
| Q132 | - |  |  | SI | Quality of movement |
| Q133 | - |  |  | SI | Passive Range of Motion Analysis |
| Q134 | - |  |  | SI | Sensation |
| Q135 | - |  |  | SI | Proprioception |
| Q136 | - |  |  | SI | Please use in conjunction with the questionnaire, ... |
| Q137 | - |  |  | SI | Passive range of motion |
| Q138 | - |  |  | SI | Patient observations |
| Q139 | - |  |  | SI | Rapid alternating movements (bilateral integration... |
| Q14 | - |  |  | SI | Pick up the cup and take it to your mouth, shoulde... |
| Q140 | - |  |  | SI | Opposition (bilateral integration) |
| Q142 | - |  |  | SI | Has the Management Tool for Acute Hemiplegic Shoul... |
| Q143 | - |  |  | SI | Date |
| Q144 | - |  |  | SI | Time |
| Q145 | - |  |  | SI | Please refer to supplementary paper documents as r... |
| Q15 | - |  |  | SI | Pick up the cup and take it to your mouth, shoulde... |
| Q16 | - |  |  | SI | Pick up the cup and take it to your mouth, shoulde... |
| Q17 | - |  |  | SI | Pick up the cup and take it to your mouth, elbow e... |
| Q18 | - |  |  | SI | Pick up the cup and take it to your mouth, elbow e... |
| Q19 | - |  |  | SI | Pick up the cup and take it to your mouth, elbow e... |
| Q20 | - |  |  | SI | Pick up the cup and take it to your mouth, wrist e... |
| Q21 | - |  |  | SI | Pick up the cup and take it to your mouth, wrist e... |
| Q22 | - |  |  | SI | Pick up the cup and take it to your mouth, wrist e... |
| Q23 | - |  |  | SI | Pick up the cup and take it to your mouth, pre sha... |
| Q24 | - |  |  | SI | Pick up the cup and take it to your mouth, pre sha... |
| Q25 | - |  |  | SI | Pick up the cup and take it to your mouth, pre sha... |
| Q26 | - |  |  | SI | Pick up the cup and take it to your mouth, grasp (... |
| Q27 | - |  |  | SI | Pick up the cup and take it to your mouth, grasp (... |
| Q28 | - |  |  | SI | Pick up the cup and take it to your mouth, grasp (... |
| Q29 | - |  |  | SI | Pick up the cup and take it to your mouth, elbow f... |
| Q30 | - |  |  | SI | Pick up the cup and take it to your mouth, elbow f... |
| Q31 | - |  |  | SI | Pick up the cup and take it to your mouth, elbow f... |
| Q32 | - |  |  | SI | Pick up the cup and take it to your mouth, release... |
| Q33 | - |  |  | SI | Pick up the cup and take it to your mouth, release... |
| Q34 | - |  |  | SI | Pick up the cup and take it to your mouth, release... |
| Q35 | - |  |  | SI | Write your name with a pen, shoulder forward flexi... |
| Q36 | - |  |  | SI | Write your name with a pen, shoulder forward flexi... |
| Q37 | - |  |  | SI | Write your name with a pen, shoulder forward flexi... |
| Q38 | - |  |  | SI | Write your name with a pen, shoulder external rota... |
| Q39 | - |  |  | SI | Write your name with a pen, shoulder external rota... |
| Q40 | - |  |  | SI | Write your name with a pen, shoulder external rota... |
| Q41 | - |  |  | SI | Write your name with a pen, elbow extension (left) |
| Q42 | - |  |  | SI | Write your name with a pen, elbow extension (right... |
| Q43 | - |  |  | SI | Write your name with a pen, elbow extension (quali... |
| Q44 | - |  |  | SI | Write your name with a pen, grasp (left) |
| Q45 | - |  |  | SI | Write your name with a pen, grasp (right) |
| Q46 | - |  |  | SI | Write your name with a pen, grasp (quality of move... |
| Q47 | - |  |  | SI | Write your name with a pen, In hand manipulation (... |
| Q48 | - |  |  | SI | Write your name with a pen, In hand manipulation (... |
| Q49 | - |  |  | SI | Write your name with a pen, In hand manipulation (... |
| Q50 | - |  |  | SI | Turn over paper / newspaper, shoulder forward flex... |
| Q51 | - |  |  | SI | Turn over paper / newspaper, shoulder forward flex... |
| Q52 | - |  |  | SI | Turn over paper / newspaper, shoulder forward flex... |
| Q53 | - |  |  | SI | Turn over paper / newspaper, pronation (left) |
| Q54 | - |  |  | SI | Turn over paper / newspaper, pronation (right) |
| Q55 | - |  |  | SI | Turn over paper / newspaper, pronation (quality of... |
| Q56 | - |  |  | SI | Turn over paper / newspaper, supination (left) |
| Q57 | - |  |  | SI | Turn over paper / newspaper, supination (right) |
| Q58 | - |  |  | SI | Turn over paper / newspaper, supination (quality o... |
| Q59 | - |  |  | SI | Motion active range observation |
| Q60 | - |  |  | SI | Passive range of motion |
| Q61 | - |  |  | SI | Functional grasps (left) |
| Q62 | - |  |  | SI | Functional grasps (right) |
| Q63 | - |  |  | SI | Functional grasps (quality of movement) |
| Q64 | - |  |  | SI | Grip strength (left) |
| Q65 | - |  |  | SI | Grip strength (right) |
| Q66 | - |  |  | SI | Grip strength (quality of movement) |
| Q67 | - |  |  | SI | Patient's observations |
| Q68 | - |  |  | SI | Rapid alternating movements (left) |
| Q69 | - |  |  | SI | Rapid alternating movements (right) |
| Q70 | - |  |  | SI | Rapid alternating movements (bilateral integration... |
| Q71 | - |  |  | SI | Rapid alternating movements |
| Q72 | - |  |  | SI | Finger – nose (left) |
| Q73 | - |  |  | SI | Finger – Nose (Right) |
| Q74 | - |  |  | SI | N/A |
| Q75 | - |  |  | SI | Finger – nose |
| Q76 | - |  |  | SI | Opposition (left) |
| Q77 | - |  |  | SI | Opposition (right) |
| Q78 | - |  |  | SI | Opposition (bilateral integration) |
| Q79 | - |  |  | SI | Opposition |
| Q80 | - |  |  | SI | Sensation light touch |
| Q81 | - |  |  | SI | Proprioception shoulder |
| Q82 | - |  |  | SI | Proprioception elbow |
| Q83 | - |  |  | SI | Proprioception wrist |
| Q84 | - |  |  | SI | Proprioception fingers |
| Q85 | - |  |  | SI | Issues identified |
| Q86 | - |  |  | SI | Recommendations / Plan |
| Q87 | - |  |  | SI | Handwrite name: the patient writes his name |
| Q88 | - |  |  | SI | Occupational therapist name |
| Q89 | - |  |  | SI | Date |
| Q90 | - |  |  | SI | Signature |
| Q90UDt | - |  |  | SI | Signature Last Updated Date |
| Q90UTm | - |  |  | SI | Signature Last Updated Time |
| Q91 | - |  |  | SI | Pick up the cup and take it to your mouth |
| Q92 | - |  |  | SI | Left |
| Q93 | - |  |  | SI | Right |
| Q94 | - |  |  | SI | Quality of movement |
| Q95 | - |  |  | SI | Shoulder forward flexion |
| Q96 | - |  |  | SI | Elbow extension |
| Q97 | - |  |  | SI | Wrist extension |
| Q98 | - |  |  | SI | Pre shaping of the fingers |
| Q99 | - |  |  | SI | Grasp |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*