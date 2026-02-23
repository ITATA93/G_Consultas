# SQLUser.PAC_LeaveCategory

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LEACAT_RowId | bigint | PK |  | NO | - |
| LEACAT_Code | varchar |  |  | NO | Code |
| LEACAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LEACAT_ContractedCare | varchar |  |  | SI | ContractedCare |
| LEACAT_CreatedDate | date |  |  | SI | Created Date |
| LEACAT_CreatedTime | time |  |  | SI | Created Time |
| LEACAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LEACAT_DateFrom | date |  |  | SI | Date From |
| LEACAT_DateTo | date |  |  | SI | Date To |
| LEACAT_Desc | varchar |  |  | NO | Description |
| LEACAT_Owner | varchar |  |  | SI | Owner |
| LEACAT_PsychatricCare | varchar |  |  | SI | [DEPRECATED]Replaced by mental health module in Tr... |
| LEACAT_UpdatedDate | date |  |  | SI | Updated Date |
| LEACAT_UpdatedTime | time |  |  | SI | Updated Time |
| LEACAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Have the following topics been discussed?	 |
| Q02 | - |  |  | SI | More likely to have your babies earlier	 |
| Q03 | - |  |  | SI | Dichorionic / Diamniotic aim for delivery after 37... |
| Q04 | - |  |  | SI | Monochorionic / Diamniotic aim for delivery after ... |
| Q05 | - |  |  | SI | Monochorionic / Monoamniotic aim for delivery at 3... |
| Q06 | - |  |  | SI | Notes	 |
| Q07 | - |  |  | SI | Vaginal birth is usual if twin 1 is cephalic (Dich... |
| Q08 | - |  |  | SI | Continuous monitoring during labour	 |
| Q09 | - |  |  | SI | Twin 1 may have Fetal Scalp Electrode applied	 |
| Q10 | - |  |  | SI | Procedure following birth of Twin 1	 |
| Q11 | - |  |  | SI | Twin 2 non-cephalic complex interventions may be r... |
| Q12 | - |  |  | SI | Risk of Caesarean section if twin 2 is small (<3%)... |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Elective Caesarean section  for Twin 1 Breech	 |
| Q15 | - |  |  | SI | Elective Caesarean section  for Twin 1 Placenta Pr... |
| Q16 | - |  |  | SI | Elective Caesarean section  - Maternal choice	 |
| Q17 | - |  |  | SI | Notes |
| Q18 | - |  |  | SI | Risk of bleeding	 |
| Q19 | - |  |  | SI | Risk of bladder damage	 |
| Q20 | - |  |  | SI | Risk of wound infection	 |
| Q21 | - |  |  | SI | Risk of thrombosis	 |
| Q22 | - |  |  | SI | Longer hospital stay may be required	 |
| Q23 | - |  |  | SI | Babies may have 'wet lung' and require special car... |
| Q24 | - |  |  | SI | Longer recovery and driving restrictions	 |
| Q25 | - |  |  | SI | May affect future birth options	 |
| Q26 | - |  |  | SI | Can make breast feeding more difficult	 |
| Q27 | - |  |  | SI | May avoid complex delivery of Twin 2 if not cephal... |
| Q28 | - |  |  | SI | Avoids Emergency Caesarean section which may occur... |
| Q29 | - |  |  | SI | Notes |
| Q30 | - |  |  | SI | Pain relief in labour leaflet given	 |
| Q31 | - |  |  | SI | Epidural anaesthesia discussed	 |
| Q32 | - |  |  | SI | Notes |
| Q33 | - |  |  | SI | Advised re: number of health professionals present... |
| Q34 | - |  |  | SI | Increase risk of admission to Neonatal Unit	 |
| Q35 | - |  |  | SI | Preferred mode of birth	 |
| Q36 | - |  |  | SI | Contingency Plan	 |
| Q37 | - |  |  | SI | Notes	 |
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