# SQLUser.LB_RequestSpecimenContainer

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRQSPC_RowID | bigint | PK |  | NO | - |
| LBRQCSPC_TestSetRevisionItems | varchar |  |  | SI | List of Request Test Sets Items that can be perfor... |
| LBRQSPC_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBRQSPC_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBRQSPC_Collected | varchar |  |  | SI | Specimen Collected |
| LBRQSPC_CollectedBy_DR | bigint |  | FK | SI | User Who Collected the Specimen Container  |
| LBRQSPC_CollectionCentre_DR | bigint |  | FK | SI | Collection Centre |
| LBRQSPC_CollectionDate | date |  |  | SI | Date Of Collection of the sample |
| LBRQSPC_CollectionSpecimenContainers | varchar |  |  | SI | List of collections that intitated the creation of... |
| LBRQSPC_CollectionTime | time |  |  | SI | Time Of Collection of the sample |
| LBRQSPC_Comments | varchar |  |  | SI | Comments |
| LBRQSPC_ContainerNumber | varchar |  |  | SI | Container Number (from manufacturer) |
| LBRQSPC_Container_DR | bigint |  | FK | SI | Container Type |
| LBRQSPC_CrossDepartment | bit |  |  | SI | Indicates if specimen container can be used by mul... |
| LBRQSPC_DepartmentIndicator | varchar |  |  | SI | Specimen Container Department Indicator
Used for ... |
| LBRQSPC_FinalDestination | varchar |  |  | SI | If there are transfers for this specimen container... |
| LBRQSPC_Initiation_DR | bigint |  | FK | SI | Initiation |
| LBRQSPC_LabSite_DR | bigint |  | FK | SI | Lab site of the specimen container |
| LBRQSPC_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBRQSPC_ManualSpecimenEntry | varchar |  |  | SI | Manual Specimen Entry |
| LBRQSPC_ReceivedBy_DR | bigint |  | FK | SI | ser Who Received the Specimen Container  |
| LBRQSPC_ReceivedDate | date |  |  | SI | Date Of Receiving |
| LBRQSPC_ReceivedTime | time |  |  | SI | Time Of Receiving |
| LBRQSPC_Request_DR | bigint |  | FK | NO | Lab Request |
| LBRQSPC_ReusableForOtherLocations | bit |  |  | SI | Indicates if the specimen container can be reused ... |
| LBRQSPC_SpecimenNumber | varchar |  |  | SI | Specimen Number |
| LBRQSPC_Specimen_DR | bigint |  | FK | SI | Specimen Type |
| LBRQSPC_VolumeCollected | double |  |  | SI | Actual volume collected in the Container |
| LBRQSPC_VolumeCurrently | double |  |  | SI | Current volume remaining in the Container |
| LBRQSPC_VolumeNeeded | double |  |  | SI | Original volume needed |
| Q01 | - |  |  | SI | Expresión Facial |
| Q02 | - |  |  | SI | Piernas |
| Q03 | - |  |  | SI | Actividad |
| Q04 | - |  |  | SI | Llanto |
| Q05 | - |  |  | SI | Consuelo |
| Q06 | - |  |  | SI | Puntaje Escala FLACC |
| Q06ObsDR | - |  |  | SI | Puntaje Escala FLACC DR |
| Q07 | - |  |  | SI | Resultado Escala FLACC |
| Q07ObsDR | - |  |  | SI | Resultado Escala FLACC DR |
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