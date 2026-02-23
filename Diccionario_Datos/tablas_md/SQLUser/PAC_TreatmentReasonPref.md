# SQLUser.PAC_TreatmentReasonPref

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACTP_ParRef | bigint | PK |  | NO | PACTreatmentReason Parent Reference |
| PACTP_CarPrvTp_DR | bigint |  | FK | SI | Des Ref CTCarPrvTp |
| PACTP_Childsub | double |  |  | NO | Childsub |
| PACTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACTP_CreatedDate | date |  |  | SI | Created Date |
| PACTP_CreatedTime | time |  |  | SI | Created Time |
| PACTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACTP_Issues | varchar |  |  | SI | List of NRCIssues |
| PACTP_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| PACTP_RowId | varchar |  |  | NO | - |
| PACTP_UpdatedDate | date |  |  | SI | Updated Date |
| PACTP_UpdatedTime | time |  |  | SI | Updated Time |
| PACTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Interventional procedure |
| Q04 | - |  |  | SI | Pregnant? |
| Q05 | - |  |  | SI | Last menstrual period |
| Q06 | - |  |  | SI | Infection prevention |
| Q07 | - |  |  | SI | Are you immuno-compromised, or have you previously... |
| Q08 | - |  |  | SI | Have you had any symptoms of infection (E.g. cough... |
| Q09 | - |  |  | SI | Have you taken antibiotics within the last 3 month... |
| Q10 | - |  |  | SI | Do you have any exfoliating skin conditions such a... |
| Q11 | - |  |  | SI | Do you have MRSA or have you previously been ident... |
| Q12 | - |  |  | SI | Have you ever been treated for or advised you have... |
| Q13 | - |  |  | SI | Have you had diarrhoea (loose stools) in the last ... |
| Q14 | - |  |  | SI | Have you or anyone in your family been diagnosed w... |
| Q15 | - |  |  | SI | Have you anything in your medical, personal or soc... |
| Q16 | - |  |  | SI | Do you have any body piercings? |
| Q17 | - |  |  | SI | If yes to any of the above please detail |
| Q18 | - |  |  | SI | Known risk factors |
| Q19 | - |  |  | SI | If other, please record details |
| Q20 | - |  |  | SI | Allergy status recorded? |
| Q21 | - |  |  | SI | Medications prescribed and administered? |
| Q22 | - |  |  | SI | Specimens taken? |
| Q23 | - |  |  | SI | If yes, please detail |
| Q24 | - |  |  | SI | Number of specimens |
| Q25 | - |  |  | SI | Type of specimens |
| Q26 | - |  |  | SI | Additional details |
| Q27 | - |  |  | SI | Care provider |
| Q28 | - |  |  | SI | Additional details |
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