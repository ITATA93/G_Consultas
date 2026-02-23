# SQLUser.PAC_DischargeDestination

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DDEST_RowId | bigint | PK |  | NO | - |
| DDEST_CareAvailab | varchar |  |  | SI | CareAvailab |
| DDEST_CareType | varchar |  |  | SI | CareType |
| DDEST_Code | varchar |  |  | NO | Code |
| DDEST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DDEST_CreatedDate | date |  |  | SI | Created Date |
| DDEST_CreatedTime | time |  |  | SI | Created Time |
| DDEST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DDEST_CriticalCareTransfer | varchar |  |  | SI | CriticalCareTransfer |
| DDEST_DateFrom | date |  |  | SI | Date From |
| DDEST_DateTo | date |  |  | SI | Date To |
| DDEST_Desc | varchar |  |  | NO | Description |
| DDEST_IconName | varchar |  |  | SI | Icon Name |
| DDEST_IconPriority | varchar |  |  | SI | Icon Priority |
| DDEST_IntentReadmit | varchar |  |  | SI | IntentReadmit |
| DDEST_NationalCode | varchar |  |  | SI | National Code |
| DDEST_Owner | varchar |  |  | SI | Owner |
| DDEST_SeparReferral | varchar |  |  | SI | SeparReferral |
| DDEST_StatisticalDischarge | varchar |  |  | SI | Statistical Discharge |
| DDEST_TransferSource | varchar |  |  | SI | Transfer Source |
| DDEST_UpdatedDate | date |  |  | SI | Updated Date |
| DDEST_UpdatedTime | time |  |  | SI | Updated Time |
| DDEST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Mallampati score III - IV |
| Q04 | - |  |  | SI | Mouth opening < 3 Pt. finger |
| Q05 | - |  |  | SI | Reduced mobility of cervical spine |
| Q06 | - |  |  | SI | Obstructive sleep apnea syndrome (OSA) |
| Q07 | - |  |  | SI | Coma |
| Q08 | - |  |  | SI | Severe hypoxemia SPO2 < 80% on room air |
| Q09 | - |  |  | SI | Non anesthesiologist |
| Q10 | - |  |  | SI | Physician signature |
| Q10UDt | - |  |  | SI | Physician signature Last Updated Date |
| Q10UTm | - |  |  | SI | Physician signature Last Updated Time |
| Q11 | - |  |  | SI | Date |
| Q12 | - |  |  | SI | Time |
| Q13 | - |  |  | SI | Physician's name |
| Q14 | - |  |  | SI | Score |
| Q15 | - |  |  | SI | Classification |
| Q16 | - |  |  | SI | 0 - 4 |
| Q17 | - |  |  | SI | Easy intubation |
| Q18 | - |  |  | SI | ≥ 5 |
| Q19 | - |  |  | SI | Suspected to be difficult intubation |
| Q20 | - |  |  | SI | 0 - 4: Easy intubation |
| Q21 | - |  |  | SI | ≥ 5: Suspected to be difficult intubation |
| Q22 | - |  |  | SI | MACOCHA scoring tool provides a provision to predi... |
| Q23 | - |  |  | SI | The Mallampati Score |
| Q24 | - |  |  | SI | Complete visualization of the soft palate |
| Q25 | - |  |  | SI | Complete visualization of the uvula |
| Q26 | - |  |  | SI | Visualization of only the base of the uvula |
| Q27 | - |  |  | SI | Soft palate is not visible at all |
| Q28 | - |  |  | SI | Class 1 |
| Q29 | - |  |  | SI | Class 2 |
| Q30 | - |  |  | SI | Class 3 |
| Q31 | - |  |  | SI | Class 4 |
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