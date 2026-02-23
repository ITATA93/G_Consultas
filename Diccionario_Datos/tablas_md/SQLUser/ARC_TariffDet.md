# SQLUser.ARC_TariffDet

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | ARC_Tariff Parent Reference |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref EpisodeSubType |
| DET_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| DET_Rank | double |  |  | SI | Rank |
| DET_RowId | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | I. Movimiento Grueso |
| Q04 | - |  |  | SI | 1. Abducción hombros hasta la altura de los hombro... |
| Q05 | - |  |  | SI | 1. Abducción hombros hasta la altura de los hombro... |
| Q06 | - |  |  | SI | 2. Abducción hombro sobre la altura de los hombros... |
| Q07 | - |  |  | SI | 2. Abducción hombro sobre la altura de los hombros... |
| Q08 | - |  |  | SI | 3. Flexión de hombros hasta altura de los hombros ... |
| Q09 | - |  |  | SI | 3. Flexión de hombros hasta altura de los hombros ... |
| Q10 | - |  |  | SI | 4. Flexión de hombros sobre altura de los hombros ... |
| Q11 | - |  |  | SI | 4. Flexión de hombros sobre altura de los hombros ... |
| Q12 | - |  |  | SI | 5. Colocar mano a la boca (Derecha) |
| Q13 | - |  |  | SI | 5. Colocar mano a la boca (Izquierda) |
| Q14 | - |  |  | SI | 6. Colocar mano en la nuca (Derecha) |
| Q15 | - |  |  | SI | 6. Colocar mano en la nuca (Izquierda) |
| Q16 | - |  |  | SI | 7. Trasladar un objetivo desde los muslos a mesa a... |
| Q17 | - |  |  | SI | 7. Trasladar un objetivo desde los muslos a mesa a... |
| Q18 | - |  |  | SI | 8. Levantar y trasladar botella de agua 500 cc. (D... |
| Q19 | - |  |  | SI | 8. Levantar y trasladar botella de agua 500 cc. (I... |
| Q20 | - |  |  | SI | II. Pinzas |
| Q21 | - |  |  | SI | 1. Cortar papel en dos (Derecha) |
| Q22 | - |  |  | SI | 1. Cortar papel en dos (Izquierda) |
| Q23 | - |  |  | SI | 2. Destapar una botella (Derecha) |
| Q24 | - |  |  | SI | 2. Destapar una botella (Izquierda) |
| Q25 | - |  |  | SI | 3. Trazar trayecto en una hoja (Derecha) |
| Q26 | - |  |  | SI | 3. Trazar trayecto en una hoja (Izquierda) |
| Q27 | - |  |  | SI | 4. Sostener tapa de vía roja entre pulgar y dedo a... |
| Q28 | - |  |  | SI | 4. Sostener tapa de vía roja entre pulgar y dedo a... |
| Q29 | - |  |  | SI | 5. Sostener tapa de vía roja entre pulgar y dedo m... |
| Q30 | - |  |  | SI | 5. Sostener tapa de vía roja entre pulgar y dedo m... |
| Q31 | - |  |  | SI | 6. Sostener tapa de vía roja entre pulgar y dedo í... |
| Q32 | - |  |  | SI | 6. Sostener tapa de vía roja entre pulgar y dedo í... |
| Q33 | - |  |  | SI | Total Evaluación Derecha |
| Q34 | - |  |  | SI | Total Evaluación Izquierda |
| Q35 | - |  |  | SI | ALTA (3) |
| Q36 | - |  |  | SI | MEDIANA (2) |
| Q37 | - |  |  | SI | BAJA (1) |
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