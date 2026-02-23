# questionnaire.QTCOTRRC

> Perioperative - Recovery Room Care

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Recovery Room Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure name |
| Q02 | date |  |  | SI | Recovery date 	 |
| Q03 | time |  |  | SI | Recovery time	 |
| Q04 | varchar |  |  | SI | Recovery practitioner 	 |
| Q05 | varchar |  |  | SI | Airway support 	 |
| Q05ObsDR | varchar |  | FK | SI | Airway support 	 DR |
| Q06 | time |  |  | SI | Extubated / airway expelled 	 |
| Q07 | varchar |  |  | SI | O2 Delivery mode 	 |
| Q07ObsDR | varchar |  | FK | SI | O2 Delivery mode 	 DR |
| Q08 | varchar |  |  | SI | Oxygen administered %	 |
| Q08ObsDR | varchar |  | FK | SI | Oxygen administered %	 DR |
| Q09 | varchar |  |  | SI | Oxygen flow (L)	 |
| Q09ObsDR | varchar |  | FK | SI | Oxygen flow (L)	 DR |
| Q10 | numeric |  |  | SI | Oxygen duration (hh:mm)	 |
| Q12 | varchar |  |  | SI | PV loss	 |
| Q12ObsDR | varchar |  | FK | SI | PV loss	 DR |
| Q13 | varchar |  |  | SI | Skin condition	 |
| Q13ObsDR | varchar |  | FK | SI | Skin condition	 DR |
| Q14 | numeric |  |  | SI | Number of drains 	 |
| Q15 | varchar |  |  | SI | Nasogastric tube 	 |
| Q16 | varchar |  |  | SI | Vacuum drain	 |
| Q17 | varchar |  |  | SI | Urinary catheter 	 |
| Q19 | varchar |  |  | SI | Analgesia used	 |
| Q20 | varchar |  |  | SI | Specify 	 |
| Q21 | varchar |  |  | SI | Assessment on admission 	 |
| Q22 | varchar |  |  | SI | Arterial used	 |
| Q23 | varchar |  |  | SI | Central used	 |
| Q24 | varchar |  |  | SI | Anaesthesia discussed	 |
| Q25 | varchar |  |  | SI | Relevant medical history	 |
| Q26 | varchar |  |  | SI | Analgesia discussed	 |
| Q27 | varchar |  |  | SI | Medication discussed	 |
| Q28 | varchar |  |  | SI | Oxygen therapy discussed	 |
| Q29 | varchar |  |  | SI | I.V. Fluids discussed	 |
| Q30 | varchar |  |  | SI | VIAD chart commenced 	 |
| Q31 | varchar |  |  | SI | Additional information 	 |
| Q32 | varchar |  |  | SI | Anaesthetic handover	 |
| Q33 | varchar |  |  | SI | Recovery practitioner 	 |
| Q34 | varchar |  |  | SI | The following items have been discussed 	 |
| Q35 | varchar |  |  | SI | Procedure discussed	 |
| Q36 | varchar |  |  | SI | Skin integrity checked 	 |
| Q37 | varchar |  |  | SI | Specify  |
| Q38 | varchar |  |  | SI | Dressings	 |
| Q39 | varchar |  |  | SI | Drains	 |
| Q40 | varchar |  |  | SI | Catheters	 |
| Q41 | varchar |  |  | SI | Analgesia / blocks	 |
| Q42 | varchar |  |  | SI | Complications	 |
| Q43 | varchar |  |  | SI | Blood loss	 |
| Q44 | varchar |  |  | SI | Allergies	 |
| Q45 | varchar |  |  | SI | Additional information	 |
| Q46 | varchar |  |  | SI | Theatre practitioner 	 |
| Q47 | varchar |  |  | SI | Recovery practitioner 	 |
| Q48 | varchar |  |  | SI | Post operative plan 	 |
| Q49 | varchar |  |  | SI | Additional information 	 |
| Q50 | varchar |  |  | SI | Surgical handover	 |
| Q51 | varchar |  |  | SI | Recovery practitioner	 |
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