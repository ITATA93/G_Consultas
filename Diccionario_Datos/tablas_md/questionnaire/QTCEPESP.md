# questionnaire.QTCEPESP

> Doc. Intra-Operatoria Proc. Específicos

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Doc. Intra-Operatoria Proc. Específicos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q0141 | varchar |  |  | SI | Otro |
| Q0242 | varchar |  |  | SI | Otro |
| Q0243 | varchar |  |  | SI | Otros |
| Q0344 | varchar |  |  | SI | Comentarios |
| Q0445 | varchar |  |  | SI | Otro |
| Q0446 | varchar |  |  | SI | Otros |
| Q0547 | varchar |  |  | SI | Otro |
| Q0548 | varchar |  |  | SI | Otro |
| Q060 | varchar |  |  | SI | Comentario Medicamentos |
| Q0750 | varchar |  |  | SI | Comentarios |
| Q10 | varchar |  |  | SI | Posición del Paciente |
| Q11 | varchar |  |  | SI | Dispositivos para Posición |
| Q12 | varchar |  |  | SI | Prevención de UPP |
| Q13 | varchar |  |  | SI | Otras |
| Q14 | varchar |  |  | SI | Puntos de Apoyo Protegidos |
| Q15 | varchar |  |  | SI | Otro |
| Q16 | varchar |  |  | SI | Prevención TVP |
| Q17 | varchar |  |  | SI | Otro |
| Q18 | varchar |  |  | SI | Item |
| Q19 | varchar |  |  | SI | Otro |
| Q20 | varchar |  |  | SI | Descripción de Item |
| Q21 | date |  |  | SI | Fecha de Vencimiento |
| Q22 | varchar |  |  | SI | Control de Viraje |
| Q23 | varchar |  |  | SI | APÓSITOS Y VENDAJES |
| Q24 | varchar |  |  | SI | Herida Operatoria (Ejemplo: Abdomen) |
| Q25 | varchar |  |  | SI | Tipo Apósito/Vendaje |
| Q26 | varchar |  |  | SI | Condición Apósito/Vendaje |
| Q27 | varchar |  |  | SI | CAUTERIZACIÓN |
| Q28 | varchar |  |  | SI | Tipo de Generador Electroquirúrgico |
| Q29 | varchar |  |  | SI | Energía Utilizada |
| Q30 | varchar |  |  | SI | Localización de Placa Electrobisturí |
| Q31 | varchar |  |  | SI | Responsable de la Colocación Electrobisturí |
| Q32 | varchar |  |  | SI | RECUENTO INCORRECTO |
| Q33 | varchar |  |  | SI | Items Recuento Incorrecto |
| Q34 | varchar |  |  | SI | Acción Recuento Incorrecto |
| Q35 | varchar |  |  | SI | USO DE IRRIGACIÓN |
| Q36 | varchar |  |  | SI | Solución de Irrigación |
| Q37 | varchar |  |  | SI | Otro |
| Q38 | numeric |  |  | SI | Volumen Total de Entrada (ML) |
| Q39 | numeric |  |  | SI | Volumen Total de Salida (ML) |
| Q40 | varchar |  |  | SI | Medicamentos |
| Q49 | varchar |  |  | SI | Responsable del Recuento |
| Q52 | varchar |  |  | SI | Tipo de Láser |
| Q53 | varchar |  |  | SI | Modo de Láser |
| Q54 | varchar |  |  | SI | Otro |
| Q55 | varchar |  |  | SI | Refigerante Utilizado |
| Q56 | varchar |  |  | SI | Potencia |
| Q57 | varchar |  |  | SI | Total Uso de Láser |
| Q58 | varchar |  |  | SI | Seguridad Láser |
| Q59 | varchar |  |  | SI | Otro |
| Q60 | varchar |  |  | SI | Ubicación Mango Isquemia |
| Q61 | varchar |  |  | SI | 2. Posición del Paciente |
| Q62 | varchar |  |  | SI | Dispositivos para Posición |
| Q63 | varchar |  |  | SI | Profilaxis Mecánica |
| Q64 | varchar |  |  | SI | Profilaxis Farmacológica |
| Q65 | bit |  |  | SI | No Aplica (TVP) |
| Q66 | varchar |  |  | SI | Observaciones (TVP) |
| Q67 | varchar |  |  | SI | Responsable Operador Monitor Electrobisturí  |
| Q68 | varchar |  |  | SI | Nombre del Cirujano que se Notifico |
| Q69 | varchar |  |  | SI | Otros |
| Q70 | varchar |  |  | SI | Nombre de los Medicamentos  |
| Q71 | varchar |  |  | SI | Cierre de Herida Operatoria |
| Q75 | varchar |  |  | SI | 10. Transfusiones |
| Q77 | varchar |  |  | SI | Protección Ocular |
| Q78 | varchar |  |  | SI | Operador |
| Q79 | varchar |  |  | SI | Dispositivo de prevención de la hipotermia |
| Q80 | varchar |  |  | SI | Nombre del Dispositivo |
| Q81 | numeric |  |  | SI | Temperatura |
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