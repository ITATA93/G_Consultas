# SQLUser.PAC_IntentionReadmit

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTREA_RowId | bigint | PK |  | NO | - |
| INTREA_Code | varchar |  |  | SI | Code |
| INTREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INTREA_CreatedDate | date |  |  | SI | Created Date |
| INTREA_CreatedTime | time |  |  | SI | Created Time |
| INTREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INTREA_DateFrom | date |  |  | SI | Date From |
| INTREA_DateTo | date |  |  | SI | Date To |
| INTREA_Default | varchar |  |  | SI | Default |
| INTREA_Desc | varchar |  |  | SI | Description |
| INTREA_DisDest | varchar |  |  | SI | DisDest |
| INTREA_NationCode | varchar |  |  | SI | National Code |
| INTREA_Owner | varchar |  |  | SI | Owner |
| INTREA_UpdatedDate | date |  |  | SI | Updated Date |
| INTREA_UpdatedTime | time |  |  | SI | Updated Time |
| INTREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Duration	 |
| Q02 | - |  |  | SI | Restraint to prevent |
| Q03 | - |  |  | SI | Prevention strategies attempted |
| Q04 | - |  |  | SI | Comments |
| Q05 | - |  |  | SI | Is specialling required |
| Q06 | - |  |  | SI | Decision discussed with |
| Q07 | - |  |  | SI | Date family involved	 |
| Q08 | - |  |  | SI | Time family involved	 |
| Q09 | - |  |  | SI | Staff member advising family	 |
| Q10 | - |  |  | SI | Form of restraint to be used |
| Q11 | - |  |  | SI | If other, please specify	 |
| Q12 | - |  |  | SI | Restraints applied to |
| Q13 | - |  |  | SI | Please specify which limbs	 |
| Q14 | - |  |  | SI | Date restraint commenced	 |
| Q15 | - |  |  | SI | Time restraint commenced	 |
| Q16 | - |  |  | SI | Nurse in charge when restraint commenced	 |
| Q17 | - |  |  | SI | Nurse in charge signature	 |
| Q17UDt | - |  |  | SI | Nurse in charge signature	 Last Updated Date |
| Q17UTm | - |  |  | SI | Nurse in charge signature	 Last Updated Time |
| Q18 | - |  |  | SI | Restraint Order (Registrar Level or Above) |
| Q19 | - |  |  | SI | Medical assessment documented	 |
| Q20 | - |  |  | SI | Frequency of Medical Review, maximum of 4 hourly |
| Q21 | - |  |  | SI | Frequency of medical review |
| Q22 | - |  |  | SI | Specific orders (eg SOOB only)	 |
| Q23 | - |  |  | SI | Review date	 |
| Q24 | - |  |  | SI | Medical officer ordering restraint	 |
| Q25 | - |  |  | SI | Medical officer signature	 |
| Q25UDt | - |  |  | SI | Medical officer signature	 Last Updated Date |
| Q25UTm | - |  |  | SI | Medical officer signature	 Last Updated Time |
| Q26 | - |  |  | SI | Name of the family member advised |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Time |
| Q29 | - |  |  | SI | Date and time of next medical review |
| Q30 | - |  |  | SI | Time |
| Q31 | - |  |  | SI | Frequency of medical review (hrs) |
| Q32 | - |  |  | SI | Is the patient under the Mental Health Act |
| Q33 | - |  |  | SI | Please complete required forms |
| Q34 | - |  |  | SI | Restraint to prevent |
| Q35 | - |  |  | SI | Other restraint to prevent |
| Q36 | - |  |  | SI | Context of the restraint |
| Q37 | - |  |  | SI | Comments |
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