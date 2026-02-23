# SQLUser.LB_StorageContainer

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSTC_RowID | bigint | PK |  | NO | - |
| LBSTC_Disposed | varchar |  |  | SI | Disposed |
| LBSTC_EndDate | date |  |  | SI | End Date |
| LBSTC_ExtendedDate | date |  |  | SI | Extended Date |
| LBSTC_Full | varchar |  |  | SI | Closed |
| LBSTC_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBSTC_MaterialTypeList | varchar |  |  | SI | Material List
The storage container may only hold... |
| LBSTC_Specimen_DR | varchar |  | FK | SI | Specimen List
The storage container may only hold... |
| LBSTC_StartDate | date |  |  | SI | Start Date |
| LBSTC_StorageContainer_DR | bigint |  | FK | SI | Container DR |
| LBSTC_Storage_DR | bigint |  | FK | SI | Storage DR |
| Q01 | - |  |  | SI | Bochornos, sudoración, calores. |
| Q02 | - |  |  | SI | Molestias al corazón (sentir latidos del corazón, ... |
| Q03 | - |  |  | SI | Molestias musculares y articulares (dolores de hue... |
| Q04 | - |  |  | SI | Dificultades en el sueño (insomnio, duerme poco). |
| Q05 | - |  |  | SI | Estado de ánimo depresivo (sentirse deprimida, dec... |
| Q06 | - |  |  | SI | Irritabilidad (sentirse tensa, explota fácil, sent... |
| Q07 | - |  |  | SI | Ansiedad (sentirse angustiada, temerosa, inquieta,... |
| Q08 | - |  |  | SI | Cansancio físico y mental (rinde menos, se cansa f... |
| Q09 | - |  |  | SI | Problemas sexuales (menos ganas de sexo, menor fre... |
| Q10 | - |  |  | SI | Problemas con la orina (problemas al orinar, orina... |
| Q11 | - |  |  | SI | Sequedad vaginal (sensación de genitales secos, ma... |
| Q12 | - |  |  | SI | Somático |
| Q13 | - |  |  | SI | Psicológico |
| Q14 | - |  |  | SI | Urogenital |
| Q15 | - |  |  | SI | Total |
| Q17 | - |  |  | SI | Resultado Escala MRS Dominio Somático |
| Q17ObsDR | - |  |  | SI | Resultado Escala MRS Dominio Somático DR |
| Q18 | - |  |  | SI | Resultado Escala MRS Dominio Psicológico |
| Q18ObsDR | - |  |  | SI | Resultado Escala MRS Dominio Psicológico DR |
| Q19 | - |  |  | SI | Resultado Escala MRS Dominio Urogenital |
| Q19ObsDR | - |  |  | SI | Resultado Escala MRS Dominio Urogenital DR |
| Q20 | - |  |  | SI | Resultado Escala MRS |
| Q20ObsDR | - |  |  | SI | Resultado Escala MRS DR |
| Q21 | - |  |  | SI | ¿Paciente Bajo Terapia Hormonal de Reemplazo? [REM... |
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