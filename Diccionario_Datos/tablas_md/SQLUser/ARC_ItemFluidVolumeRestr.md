# SQLUser.ARC_ItemFluidVolumeRestr

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITFVR_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| CQ1 | - |  |  | SI | (null) |
| CQ12 | - |  |  | SI | (null) |
| CQ13 | - |  |  | SI | (null) |
| CQ2 | - |  |  | SI | (null) |
| CQ3 | - |  |  | SI | (null) |
| CQ4 | - |  |  | SI | (null) |
| CQ5 | - |  |  | SI | (null) |
| CQ6 | - |  |  | SI | (null) |
| CQ7 | - |  |  | SI | (null) |
| CQ8 | - |  |  | SI | (null) |
| CQ9 | - |  |  | SI | (null) |
| ITFVR_Childsub | double |  |  | NO | Childsub |
| ITFVR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITFVR_CreatedDate | date |  |  | SI | Created Date |
| ITFVR_CreatedTime | time |  |  | SI | Created Time |
| ITFVR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITFVR_DefaultFlag | varchar |  |  | SI | Default Flag |
| ITFVR_FluidVolumeRestr_DR | bigint |  | FK | SI | Des Ref DTCFluidVolumeRestr |
| ITFVR_RowId | varchar |  |  | NO | - |
| ITFVR_UpdatedDate | date |  |  | SI | Updated Date |
| ITFVR_UpdatedTime | time |  |  | SI | Updated Time |
| ITFVR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | ¿Maneja él/ella su propio dinero? |
| Q10 | - |  |  | SI | Resultado |
| Q11 | - |  |  | SI | Resultado actividades funcionales Pfeffer |
| Q11ObsDR | - |  |  | SI | Resultado actividades funcionales Pfeffer DR |
| Q12 | - |  |  | SI | ¿Es él/ella capaz de recordar compromisos, acontec... |
| Q13 | - |  |  | SI | ¿Es él/ella capaz de pasear por el vecindario y en... |
| Q14 | - |  |  | SI | El screening es positivo cuando el puntaje es igua... |
| Q15 | - |  |  | SI | Recuerde Ingresar Resultado en Forma Manual en Cue... |
| Q2 | - |  |  | SI | ¿Es él/ella capaz de comprar ropas solo, cosas par... |
| Q3 | - |  |  | SI | ¿Es él/ella capaz de calentar agua para el café o ... |
| Q4 | - |  |  | SI | ¿Es él/ella capaz de preparar una comida? |
| Q5 | - |  |  | SI | ¿Es él/ella de mantenerse al tanto de los aconteci... |
| Q6 | - |  |  | SI | ¿Es él/ella capaz de poner atención y entender y d... |
| Q7 | - |  |  | SI | ¿Es él/ella capaz de manejar sus propios medicamen... |
| Q8 | - |  |  | SI | ¿Es él/ella capaz de saludar a sus amigos adecuada... |
| Q9 | - |  |  | SI | ¿Puede él/ella ser dejado en casa en forma segura? |
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