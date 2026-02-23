# SQLUser.LB_EpisodeReportingInterface

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPRI_ParRef | varchar | PK |  | NO | - |
| LBEPRI_Copies | numeric |  |  | SI | Number of Copies
0 = do not produce report, resul... |
| LBEPRI_IsAddOn | varchar |  |  | SI | Is Add-On
N = It's entered in Lab Registration
Y... |
| LBEPRI_Queue_DR | bigint |  | FK | SI | External Interface Queue |
| LBEPRI_ReportMode | varchar |  |  | SI | Report Mode |
| LBEPRI_RowID | varchar |  |  | NO | - |
| LBEPRI_TestSets | varchar |  |  | SI | A list of test sets using the report interface (On... |
| Q01 | - |  |  | SI | Sexo |
| Q02 | - |  |  | SI | Ambulatorio |
| Q03 | - |  |  | SI | Hospitalizado |
| Q04 | - |  |  | SI | Embarazada |
| Q05 | - |  |  | SI | No ha iniciado TARV |
| Q06 | - |  |  | SI | TRAV Suspendida |
| Q07 | - |  |  | SI | Actualmente en TARV |
| Q08 | - |  |  | SI | Fecha de Inicio |
| Q09 | - |  |  | SI | Marcar drogas de TARV actual: |
| Q10 | - |  |  | SI | Otro antiretroviral (indicar) |
| Q11 | - |  |  | SI | Fecha de extracción de muestra |
| Q12 | - |  |  | SI | Hora |
| Q13 | - |  |  | SI | Responsable |
| Q14 | - |  |  | SI | Fecha de Lisis |
| Q15 | - |  |  | SI | Vol. Plasma en T. Lisis (ml) |
| Q16 | - |  |  | SI | Muestra enviada |
| Q17 | - |  |  | SI | Establecimiento |
| Q18 | - |  |  | SI | Medico Solicitante |
| Q19 | - |  |  | SI | FechaM |
| Q20 | - |  |  | SI | Observaciones |
| Q21 | - |  |  | SI | Fecha |
| Q22 | - |  |  | SI | Hora |
| Q23 | - |  |  | SI | Responsable |
| Q24 | - |  |  | SI | Observación |
| Q29 | - |  |  | SI | Inicial del 1° nombre, iniciales 1° y 2° apellido ... |
| Q30 | - |  |  | SI | Clasificación |
| Q31 | - |  |  | SI | Fecha de Suspensión |
| Q32 | - |  |  | SI | Unidad |
| Q33 | - |  |  | SI | Establecimiento |
| Q34 | - |  |  | SI | N° Solicitud |
| Q35 | - |  |  | SI | N° CONFIRM.ISP |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*