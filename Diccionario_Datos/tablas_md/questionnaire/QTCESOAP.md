# questionnaire.QTCESOAP

> Accidente de Tránsito

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Accidente de Tránsito

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ04AT2 | varchar |  |  | SI | - |
| CQ08AT3 | varchar |  |  | SI | - |
| CQ15AT3 | varchar |  |  | SI | - |
| CQ18AT2 | varchar |  |  | SI | - |
| CQ20AT3 | varchar |  |  | SI | - |
| CQ21AT3 | varchar |  |  | SI | - |
| CQ23AT2 | varchar |  |  | SI | - |
| CQ24AT2 | varchar |  |  | SI | - |
| CQ25AT2 | varchar |  |  | SI | - |
| CQ26AT2 | varchar |  |  | SI | - |
| CQ27AT3 | varchar |  |  | SI | - |
| Q01AT1 | date |  |  | SI | Fecha del Accidente |
| Q02AT1 | time |  |  | SI | Hora |
| Q03AT1 | varchar |  |  | SI | Lugar del Accidente |
| Q04AT1 | varchar |  |  | SI | Unidad Policial que tomo el procedimiento_old |
| Q04AT2 | varchar |  |  | SI | Unidad Policial que Tomó el Procedimiento |
| Q05AT1 | varchar |  |  | SI | Vigencia Poliza |
| Q06AT1 | varchar |  |  | SI | Compañia de Seguro |
| Q07AT1 | varchar |  |  | SI | Comuna |
| Q08AT1 | varchar |  |  | SI | Juzgado policía Local_OLD |
| Q08AT3 | varchar |  |  | SI | Juzgado Policía Local_old2 |
| Q09AT1 | varchar |  |  | SI | Fiscalía_old |
| Q10AT1 | varchar |  |  | SI | Tipo de vehiculo_old |
| Q11AT1 | varchar |  |  | SI | N° de Poliza |
| Q12AT1 | varchar |  |  | SI | Parte |
| Q13AT2 | varchar |  |  | SI | RUN del conductor |
| Q14AT2 | varchar |  |  | SI | Patente |
| Q15AT2 | varchar |  |  | SI | Marca/Modelo_old |
| Q15AT3 | varchar |  |  | SI | Marca |
| Q16AT2 | varchar |  |  | SI | Nombre Conductor |
| Q17AT2 | varchar |  |  | SI | Licencia |
| Q18AT2 | varchar |  |  | SI | Denunciado |
| Q19AT2 | varchar |  |  | SI | Municipalidad que entrega el permiso_old |
| Q20AT2 | varchar |  |  | SI | Tipo de Accidente_old |
| Q20AT3 | varchar |  |  | SI | Tipo de Accidente |
| Q21AT2 | varchar |  |  | SI | Servicio de Salud |
| Q21AT3 | varchar |  |  | SI | ¿Conductor es menor de edad? |
| Q22AT2 | varchar |  |  | SI | Municipalidad que Entregó Permiso de Circulación |
| Q22AT3 | varchar |  |  | SI | RUN del Responsable |
| Q23AT2 | varchar |  |  | SI | Tipo de Vehículo |
| Q23AT3 | varchar |  |  | SI | Nombre del reponsable |
| Q24AT2 | varchar |  |  | SI | Fiscalia_old1 |
| Q24AT3 | varchar |  |  | SI | Dirección del responsable |
| Q25AT2 | varchar |  |  | SI | Fiscalía |
| Q25AT3 | varchar |  |  | SI | Teléfono del responsable |
| Q26AT2 | varchar |  |  | SI | Juzgado Policía Local |
| Q27AT3 | varchar |  |  | SI | Modelo |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*