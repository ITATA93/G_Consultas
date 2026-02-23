# SQLUser.PA_ORAnaestMaintenanceSnapshot

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAAMN_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAAMN_ChildSub | double |  |  | NO | Childsub |
| PAAMN_RowId | varchar |  |  | NO | - |
| PAAMN_Type_DR | bigint |  | FK | SI | Des Ref ORCAnaestheticMaintenance |
| Q01 | - |  |  | SI | COMPORTAMIENTOS DE INTERACCIÓN / COMUNICACIÓN SOCI... |
| Q02 | - |  |  | SI | A. Comunicación verbal |
| Q03 | - |  |  | SI | Ausencia de lenguaje verbal o retraso en el lengua... |
| Q04 | - |  |  | SI | Pérdida del lenguaje o habilidades sociales adquir... |
| Q05 | - |  |  | SI | No responde a su nombre |
| Q06 | - |  |  | SI | Ecolalia: repite sonidos o frases |
| Q07 | - |  |  | SI | Da respuestas no atingentes a las preguntas que se... |
| Q08 | - |  |  | SI | B. Comunicación no verbal |
| Q09 | - |  |  | SI | Ausencia o uso disminuido de gestos: saludo, negar... |
| Q10 | - |  |  | SI | Instrumentalización del adulto/a: utiliza la mano ... |
| Q11 | - |  |  | SI | Contacto visual disminuido o ausente |
| Q12 | - |  |  | SI | C. Interacción social |
| Q13 | - |  |  | SI | Tendencia a aislarse, 'muy independiente', no se i... |
| Q14 | - |  |  | SI | No indica para pedir o para mostrar/ No muestra ob... |
| Q15 | - |  |  | SI | Sonrisa social ausente o disminuida |
| Q16 | - |  |  | SI | INTERESES INUSUALES/ RESTRINGIDOS Y/O COMPORTAMIEN... |
| Q17 | - |  |  | SI | Imaginación y variedad reducida o ausente en los j... |
| Q18 | - |  |  | SI | Movimientos 'estereotipados' repetitivos como alet... |
| Q19 | - |  |  | SI | Intereses demasiado restringidos o inusuales para ... |
| Q20 | - |  |  | SI | Respuesta inusual e intensa a sonidos cotidianos, ... |
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