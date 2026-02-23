# questionnaire.QTCABCDE

> ABCDE

**Schema:** questionnaire
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(ABCDE)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Airways |
| Q01ObsDR | varchar |  | FK | SI | Airways DR |
| Q02 | varchar |  |  | SI | Instrumented |
| Q02ObsDR | varchar |  | FK | SI | Instrumented DR |
| Q03 | varchar |  |  | SI | Other |
| Q04 | varchar |  |  | SI | Inspired oxygen |
| Q04ObsDR | varchar |  | FK | SI | Inspired oxygen DR |
| Q05 | varchar |  |  | SI | Ventilation |
| Q06 | varchar |  |  | SI | Measured respiratory frequency |
| Q07 | varchar |  |  | SI | Respirations |
| Q07ObsDR | varchar |  | FK | SI | Respirations DR |
| Q08 | varchar |  |  | SI | Respiration |
| Q09 | varchar |  |  | SI | Inspection |
| Q10 | varchar |  |  | SI | Chest expansion |
| Q10ObsDR | varchar |  | FK | SI | Chest expansion DR |
| Q11 | bit |  |  | SI | Accessory muscle use |
| Q12 | bit |  |  | SI | Diaphragmatic breathing |
| Q13 | bit |  |  | SI | Paradoxical breathing |
| Q14 | varchar |  |  | SI | Flail chest |
| Q15 | varchar |  |  | SI | Laterality |
| Q16 | varchar |  |  | SI | Palpation |
| Q17 | varchar |  |  | SI | Subcutaneous emphysema |
| Q18 | varchar |  |  | SI | Parietal haematoma |
| Q19 | varchar |  |  | SI | Rib fracture evidence |
| Q20 | varchar |  |  | SI | Auscultation |
| Q21 | varchar |  |  | SI | Breath sounds |
| Q22 | varchar |  |  | SI | Absence of breath sounds |
| Q23 | varchar |  |  | SI | Inspiratory wheezes |
| Q24 | varchar |  |  | SI | Expiratory wheezes |
| Q25 | varchar |  |  | SI | Rales |
| Q26 | varchar |  |  | SI | Ronchi |
| Q27 | varchar |  |  | SI | Hb oxygen saturation |
| Q27ObsDR | varchar |  | FK | SI | Hb oxygen saturation DR |
| Q28 | bit |  |  | SI | Not assessed |
| Q29 | bit |  |  | SI | Not assessable |
| Q30 | varchar |  |  | SI | Capillary refill time |
| Q30ObsDR | varchar |  | FK | SI | Capillary refill time DR |
| Q31 | varchar |  |  | SI | Systolic blood pressure |
| Q31ObsDR | varchar |  | FK | SI | Systolic blood pressure DR |
| Q32 | varchar |  |  | SI | Diastolic blood pressure |
| Q32ObsDR | varchar |  | FK | SI | Diastolic blood pressure DR |
| Q33 | bit |  |  | SI | Not measured |
| Q34 | varchar |  |  | SI | Pulse site |
| Q35 | varchar |  |  | SI | Heart rate |
| Q35ObsDR | varchar |  | FK | SI | Heart rate DR |
| Q36 | varchar |  |  | SI | Cardiac rhythm |
| Q36ObsDR | varchar |  | FK | SI | Cardiac rhythm DR |
| Q37 | bit |  |  | SI | Asystole |
| Q38 | bit |  |  | SI | Pulseless electrical activity |
| Q39 | bit |  |  | SI | Ventricular fibrillation |
| Q40 | varchar |  |  | SI | Estimated blood loss |
| Q40ObsDR | varchar |  | FK | SI | Estimated blood loss DR |
| Q41 | varchar |  |  | SI | IV fluids |
| Q41ObsDR | varchar |  | FK | SI | IV fluids DR |
| Q42 | varchar |  |  | SI | Diuresis (in past 8 hours) |
| Q43 | varchar |  |  | SI | State of consciousness |
| Q44 | varchar |  |  | SI | Coma |
| Q44ObsDR | varchar |  | FK | SI | Coma DR |
| Q45 | varchar |  |  | SI | Pupils |
| Q46 | bit |  |  | SI | Miosis |
| Q47 | bit |  |  | SI | Mydriasis |
| Q48 | bit |  |  | SI | Anisocoria R > L |
| Q49 | bit |  |  | SI | Anisocoria L > R |
| Q50 | varchar |  |  | SI | Peripheral Nervous System |
| Q51 | varchar |  |  | SI | Hyposthenia |
| Q52 | varchar |  |  | SI | Laterality |
| Q53 | varchar |  |  | SI | Motor deficit |
| Q54 | varchar |  |  | SI | Level below |
| Q55 | varchar |  |  | SI | Sensory deficit |
| Q56 | varchar |  |  | SI | Level below |
| Q57 | varchar |  |  | SI | Blood glucose |
| Q57ObsDR | varchar |  | FK | SI | Blood glucose DR |
| Q58 | varchar |  |  | SI | Head |
| Q59 | varchar |  |  | SI | Neck |
| Q60 | varchar |  |  | SI | Thorax |
| Q61 | varchar |  |  | SI | Abdomen |
| Q62 | varchar |  |  | SI | Pelvis |
| Q63 | varchar |  |  | SI | Upper extremities |
| Q64 | varchar |  |  | SI | Lower extremities |
| Q65 | varchar |  |  | SI | Back |
| Q66 | varchar |  |  | SI | Time/Kind of last meal |
| Q67 | varchar |  |  | SI | Type of event |
| Q68 | varchar |  |  | SI | Accessory muscle use |
| Q69 | varchar |  |  | SI | Diaphragmatic breathing |
| Q70 | varchar |  |  | SI | Paradoxical breathing |
| Q71 | varchar |  |  | SI | Not assessed |
| Q72 | varchar |  |  | SI | Not assessable |
| Q73 | varchar |  |  | SI | Not measured |
| Q74 | varchar |  |  | SI | Asystole |
| Q75 | varchar |  |  | SI | Pulseless electrical activity |
| Q76 | varchar |  |  | SI | Ventricular fibrillation |
| Q77 | varchar |  |  | SI | Miosis |
| Q78 | varchar |  |  | SI | Anisocoria R > L |
| Q79 | varchar |  |  | SI | Anisocoria L > R |
| Q80 | date |  |  | SI | Date |
| Q81 | time |  |  | SI | Time |
| Q82 | varchar |  |  | SI | Mydriasis |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*