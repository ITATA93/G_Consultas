# SQLUser.PA_ComplaintServices

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SER_ParRef | bigint | PK |  | NO | PA_Complaints Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Hepatitis |
| Q04 | - |  |  | SI | Hepatitis B status |
| Q05 | - |  |  | SI | Hepatitis B status details |
| Q06 | - |  |  | SI | Hepatitis C status |
| Q07 | - |  |  | SI | Hepatitis C status details |
| Q08 | - |  |  | SI | Hepatitis C genotype |
| Q09 | - |  |  | SI | Hepatitis C genotype details |
| Q10 | - |  |  | SI | Therapy history |
| Q11 | - |  |  | SI | Co-infections |
| Q12 | - |  |  | SI | Hepatitis D status |
| Q13 | - |  |  | SI | Hepatitis D status details |
| Q14 | - |  |  | SI | Hepatitis A status |
| Q15 | - |  |  | SI | Hepatitis A status details |
| Q16 | - |  |  | SI | Extended liver screen |
| Q17 | - |  |  | SI | Extended liver screen details |
| Q18 | - |  |  | SI | Hepatitis notes |
| Q19 | - |  |  | SI | Other Viruses |
| Q20 | - |  |  | SI | HIV status |
| Q21 | - |  |  | SI | HIV status details |
| Q22 | - |  |  | SI | Cirrhosis |
| Q23 | - |  |  | SI | Cirrhosis details |
| Q24 | - |  |  | SI | Liver fibrosis |
| Q25 | - |  |  | SI | Liver fibrosis details |
| Q26 | - |  |  | SI | Fibro scan result |
| Q27 | - |  |  | SI | Hepascore |
| Q28 | - |  |  | SI | APRI score |
| Q29 | - |  |  | SI | Other virus notes |
| Q30 | - |  |  | SI | Gastroscopy Variceal Screening |
| Q31 | - |  |  | SI | Gastroscopy variceal screening required |
| Q32 | - |  |  | SI | Date of last variceal screen |
| Q33 | - |  |  | SI | Variceal screen details |
| Q34 | - |  |  | SI | Next variceal screen due |
| Q35 | - |  |  | SI | Variceal screening notes |
| Q36 | - |  |  | SI | Hepatocellular Carcinoma Screening |
| Q37 | - |  |  | SI | Hepatocellular Carcinoma (HCC) screening required |
| Q38 | - |  |  | SI | Date of last HCC screen |
| Q39 | - |  |  | SI | HHC screen details |
| Q40 | - |  |  | SI | Next HCC screen due |
| Q41 | - |  |  | SI | HCC notes |
| Q42 | - |  |  | SI | Bone Mineral Density Screening |
| Q43 | - |  |  | SI | Bone Mineral Density (BMD) screen in cirrhotic pat... |
| Q44 | - |  |  | SI | Comments on last BMD |
| Q45 | - |  |  | SI | Date of last BMD screen |
| Q46 | - |  |  | SI | BMD screen details |
| Q47 | - |  |  | SI | Next BMD screen due |
| Q48 | - |  |  | SI | BMD notes |
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
| SER_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SER_Childsub | double |  |  | NO | Childsub |
| SER_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*