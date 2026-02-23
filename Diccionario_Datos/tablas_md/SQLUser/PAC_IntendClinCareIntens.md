# SQLUser.PAC_IntendClinCareIntens

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICCI_RowId | bigint | PK |  | NO | - |
| ICCI_ActivityPoints | double |  |  | SI | Activity Points |
| ICCI_BedTypeDetails | varchar |  |  | SI | BedTypeDetails |
| ICCI_Code | varchar |  |  | NO | Code |
| ICCI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICCI_CreatedDate | date |  |  | SI | Created Date |
| ICCI_CreatedTime | time |  |  | SI | Created Time |
| ICCI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICCI_Desc | varchar |  |  | NO | Description |
| ICCI_Owner | varchar |  |  | SI | Owner |
| ICCI_UpdatedDate | date |  |  | SI | Updated Date |
| ICCI_UpdatedTime | time |  |  | SI | Updated Time |
| ICCI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | MRI Safety |
| Q02 | - |  |  | SI | Does the patient have a pacemaker or artificial he... |
| Q02a | - |  |  | SI | PLEASE NOTE - It is extremely dangerous to perform... |
| Q02b | - |  |  | SI | Is this MRI compatible / programmable? |
| Q02b1 | - |  |  | SI | The patient is incompatible for MRI – Cannot be or... |
| Q02c | - |  |  | SI | Date of insertion |
| Q02d | - |  |  | SI | Place of insertion |
| Q03 | - |  |  | SI | Does the patient have any aneurysm clips in their ... |
| Q03a | - |  |  | SI | PLEASE NOTE, It is extremely dangerous to perform ... |
| Q03b | - |  |  | SI | Date of insertion |
| Q03c | - |  |  | SI | Place of insertion |
| Q04 | - |  |  | SI | Does the patient have any electronic devices / imp... |
| Q04a | - |  |  | SI | PLEASE NOTE, Implanted electronic devices must be ... |
| Q04b | - |  |  | SI | Date of insertion |
| Q04c | - |  |  | SI | Place of insertion |
| Q05 | - |  |  | SI | Has the patient ever worked with metal filings? (e... |
| Q05a | - |  |  | SI | Has the patient ever had fragments in their eyes? |
| Q05a1 | - |  |  | SI | Please request an XR Orbits at the same time |
| Q06 | - |  |  | SI | Weight (kg) |
| Q06ObsDR | - |  |  | SI | Weight (kg) DR |
| Q07 | - |  |  | SI | Height (cm) |
| Q07ObsDR | - |  |  | SI | Height (cm) DR |
| Q08 | - |  |  | SI | BMI (kg/m2) |
| Q09 | - |  |  | SI | Has the patient had a previous MRI? |
| Q09a | - |  |  | SI | Date of MRI |
| Q09b | - |  |  | SI | Body part |
| Q10 | - |  |  | SI | Has the patient had previous surgery? |
| Q10a | - |  |  | SI | Date of surgery |
| Q10b | - |  |  | SI | Procedure (free text) |
| Q10c | - |  |  | SI | Procedure |
| Q10d | - |  |  | SI | Operation |
| Q11 | - |  |  | SI | Is the patient able to lie flat and still for 30 m... |
| Q11a | - |  |  | SI | Please, consider sedation |
| Q12 | - |  |  | SI | Is there a clip on the catheter bag drain? |
| Q12a | - |  |  | SI | Change to bag with no metal clips |
| Q13 | - |  |  | SI | Does the patient have pump drivers attached? |
| Q13a | - |  |  | SI | Must be removed prior to arrival |
| Q14 | - |  |  | SI | Renal Function |
| Q15 | - |  |  | SI | Is the patient aged over 65? |
| Q16 | - |  |  | SI | Is the patient diabetic? |
| Q17 | - |  |  | SI | Does the patient suffer from heart failure? |
| Q18 | - |  |  | SI | Does the patient have any known chronic kidney dis... |
| Q19 | - |  |  | SI | Did you answer 'Yes' to a Renal Function question? |
| Q19a | - |  |  | SI | Estimated Glomerular Filtration Rate (eGFR) level |
| Q19b | - |  |  | SI | Date of last eGFR test |
| Q19c | - |  |  | SI | Creatinine level |
| Q19d | - |  |  | SI | Date of last Creatinine test |
| Q19e | - |  |  | SI | If this test is older than 6 weeks then please ens... |
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