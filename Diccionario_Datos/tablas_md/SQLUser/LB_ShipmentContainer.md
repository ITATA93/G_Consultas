# SQLUser.LB_ShipmentContainer

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSHC_ParRef | bigint | PK |  | NO | Parent Reference |
| LBSHC_AcknowledgedBy_DR | bigint |  | FK | SI | Reference to user that acknowledges action  |
| LBSHC_CourierComment | varchar |  |  | SI | Additional user comment |
| LBSHC_Courier_DR | bigint |  | FK | SI | Reference to user |
| LBSHC_DropOffDate | date |  |  | SI | Pick-off Date |
| LBSHC_DropOffTime | time |  |  | SI | Drop-off Time |
| LBSHC_FinalDestination | varchar |  |  | SI | The property is the accumulation of the shipment c... |
| LBSHC_Number | varchar |  |  | SI | Number of the container within the shipment |
| LBSHC_PickUpDate | date |  |  | SI | Pick-up Date |
| LBSHC_PickUpTime | time |  |  | SI | Pick-up Time |
| LBSHC_ReceivedBy_DR | bigint |  | FK | SI | User Who Received the Specimen Container  |
| LBSHC_ReceivedDate | date |  |  | SI | Date Of Receiving |
| LBSHC_ReceivedTime | time |  |  | SI | Time Of Receiving |
| LBSHC_RowID | varchar |  |  | NO | - |
| LBSHC_ShipmentBarcoded | varchar |  |  | SI | Flag to indicate if all the specimen transfers wer... |
| LBSHC_Status | varchar |  |  | SI | Transaction Status of the Shipment Container |
| LBSHC_ToLabSite_DR | bigint |  | FK | SI | To Lab Site  |
| LBSHC_ToReferralLab_DR | bigint |  | FK | SI | Referral Lab Site |
| LBSHC_WorkAreaDateIn | date |  |  | SI | Date the specimen container was received into the ... |
| LBSHC_WorkAreaTimeIn | time |  |  | SI | Time the specimen container was received into the ... |
| LBSHC_WorkAreaUserIn_DR | bigint |  | FK | SI | Work Area User In
User that received the specimen... |
| LBSHC_WorkArea_DR | bigint |  | FK | SI | Current work area
Work area into which the specim... |
| Q01 | - |  |  | SI | Nombres |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | Fecha Envío |
| Q05 | - |  |  | SI | Rut |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Sexo |
| Q08 | - |  |  | SI | Previsión |
| Q09 | - |  |  | SI | Dirección |
| Q10 | - |  |  | SI | Teléfono |
| Q11 | - |  |  | SI | Profesional Responsable |
| Q12 | - |  |  | SI | Establecimiento |
| Q13 | - |  |  | SI | Unidad |
| Q14 | - |  |  | SI | Dirección |
| Q15 | - |  |  | SI | Ciudad |
| Q16 | - |  |  | SI | Teléfono |
| Q17 | - |  |  | SI | Fax |
| Q18 | - |  |  | SI | Correo |
| Q19 | - |  |  | SI | Fecha Obtención |
| Q20 | - |  |  | SI | Tipo de Muestra |
| Q21 | - |  |  | SI | Hora Obteción |
| Q22 | - |  |  | SI | ELISA |
| Q23 | - |  |  | SI | Otra |
| Q24 | - |  |  | SI | Resultado |
| Q25 | - |  |  | SI | Lectura |
| Q26 | - |  |  | SI | Punto Corte |
| Q27 | - |  |  | SI | Marca Comercial |
| Q28 | - |  |  | SI | Lote |
| Q29 | - |  |  | SI | Antecedentes Clínico / Epidemiologico |
| Q30 | - |  |  | SI | Técnica Realizada |
| Q31 | - |  |  | SI | Tipo de Muestra |
| Q32 | - |  |  | SI | Resultado |
| Q33 | - |  |  | SI | Tipo de Muestra |
| Q34 | - |  |  | SI | Técnica Realizada |
| Q35 | - |  |  | SI | Resultado |
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