# SQLUser.ORC_ClampType

**Schema:** SQLUser
**Columnas:** 136
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLMPTYPE_RowId | bigint | PK |  | NO | - |
| CLMPTYPE_Code | varchar |  |  | NO | Code |
| CLMPTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLMPTYPE_CreatedDate | date |  |  | SI | Created Date |
| CLMPTYPE_CreatedTime | time |  |  | SI | Created Time |
| CLMPTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLMPTYPE_DateFrom | date |  |  | SI | Date From |
| CLMPTYPE_DateTo | date |  |  | SI | Date To |
| CLMPTYPE_Desc | varchar |  |  | NO | Description |
| CLMPTYPE_Owner | varchar |  |  | SI | Owner |
| CLMPTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| CLMPTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| CLMPTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Posición: Supino |
| Q02 | - |  |  | SI | Observe durante todo el test. Puede descargar el s... |
| Q03 | - |  |  | SI | 1. Movimiento Espontáneo Extremidad Superior Derec... |
| Q04 | - |  |  | SI | 1. Movimiento Espontáneo Extremidad Superior Izqui... |
| Q05 | - |  |  | SI | Posición: Supino |
| Q06 | - |  |  | SI | Observe durante todo el test. Puede descargar el s... |
| Q07 | - |  |  | SI | 2. Movimiento Espontáneo Extremidad Inferior Derec... |
| Q08 | - |  |  | SI | 2. Movimiento Espontáneo Extremidad Inferior Izqui... |
| Q09 | - |  |  | SI | Posición: Supino |
| Q10 | - |  |  | SI | Fuerza de prensión: ponga su dedo en la palma del ... |
| Q11 | - |  |  | SI | May use toy of similar diameter for older children |
| Q12 | - |  |  | SI | 3. Prensión con la Mano Derecha |
| Q13 | - |  |  | SI | 3. Prensión con la Mano Izquierda |
| Q14 | - |  |  | SI | Posición: Supino |
| Q15 | - |  |  | SI | Utilice un juguete. Si el niño ya mantiene la cabe... |
| Q16 | - |  |  | SI | Place head in maximum available rotation and provi... |
| Q17 | - |  |  | SI | 4. Cabeza Línea Media&nbsp |
| Q18 | - |  |  | SI | 4. Cabeza Línea Media&nbsp |
| Q19 | - |  |  | SI | Posición: Supino, sin pañal |
| Q20 | - |  |  | SI | Caderas flexionadas, pies separados al ancho de la... |
| Q21 | - |  |  | SI | 5. Aductores de Cadera Derecha |
| Q22 | - |  |  | SI | 5. Aductores de Cadera Izquierda |
| Q23 | - |  |  | SI | Posición: Supino brazos a los costados |
| Q24 | - |  |  | SI | Test Procedure: |
| Q25 | - |  |  | SI | 1. Sosteniendo el muslo, traccionarlo con rodilla ... |
| Q26 | - |  |  | SI | 2. Si gira en esa posición tirar en 45° en diagona... |
| Q27 | - |  |  | SI | 6. Giro desde Extremidades Inferiores a Derecha |
| Q28 | - |  |  | SI | 6. Giro desde Extremidades Inferiores a Izquierda |
| Q29 | - |  |  | SI | Posición: Supino brazos a los costados |
| Q30 | - |  |  | SI | Test procedure: |
| Q31 | - |  |  | SI | 1. Tomar desde el codo y moverlo hacia el hombro c... |
| Q32 | - |  |  | SI | 2. Si logra llevar la pelvis hasta la vertical con... |
| Q33 | - |  |  | SI | 7. Giro desde Extremidades Superiores a Derecha |
| Q34 | - |  |  | SI | 7. Giro desde Extremidades Superiores a Izquierda |
| Q35 | - |  |  | SI | Posición: Decúbito lateral extremidad superior apo... |
| Q36 | - |  |  | SI | Intentar alcanzar un juguete a la altura del hombr... |
| Q37 | - |  |  | SI | (may provide stimulation and observe spontaneous m... |
| Q38 | - |  |  | SI | 8. Abducción Horizontal Derecha |
| Q39 | - |  |  | SI | 8. Abducción Horizontal Izquierda |
| Q40 | - |  |  | SI | Posición: Sentado sobre piernas o piso 20° de incl... |
| Q41 | - |  |  | SI | Presentar un objeto a la altura del hombro y al al... |
| Q42 | - |  |  | SI | (may provide stimulation and observe spontaneous m... |
| Q43 | - |  |  | SI | 9. Flexión de Hombro y Codo Derecho |
| Q44 | - |  |  | SI | 9. Flexión de Hombro y Codo Izquierdo |
| Q45 | - |  |  | SI | Posición: Sentado sobre piernas 20° de inclinación... |
| Q46 | - |  |  | SI | Estimular planta de pies con cosquillas |
| Q47 | - |  |  | SI | 10. Extensión de Rodillas Derecha |
| Q48 | - |  |  | SI | 10. Extensión de Rodillas Izquierda |
| Q49 | - |  |  | SI | Posición: Sostener al niño del tronco contra su tr... |
| Q50 | - |  |  | SI | Golpee suavemente la planta del pie del niño o est... |
| Q51 | - |  |  | SI | Test Procedure: Stroke the foot or pinch the toe |
| Q52 | - |  |  | SI | 11. Flexión de Caderas y Flexión Dorsal Derecha |
| Q53 | - |  |  | SI | 11. Flexión de Caderas y Flexión Dorsal Izquierda |
| Q54 | - |  |  | SI | Posición: Sentado con apoyo de los hombros, tronco... |
| Q55 | - |  |  | SI | Siente al niño frente a usted con las extremidades... |
| Q56 | - |  |  | SI | (may delay scoring a grade of 1 and 4 until end of... |
| Q57 | - |  |  | SI | 12. Control de Cabeza |
| Q58 | - |  |  | SI | Posición: Supino |
| Q59 | - |  |  | SI | Respuesta a la tracción: Con los brazos a 45° del ... |
| Q60 | - |  |  | SI | 13. Flexión de Codo Derecho |
| Q61 | - |  |  | SI | 13. Flexión de Codo Izquierdo |
| Q62 | - |  |  | SI | Posición: Supino |
| Q63 | - |  |  | SI | Respuesta a la tracción: Con los brazos a 45° del ... |
| Q64 | - |  |  | SI | 14. Flexión de Cuello |
| Q65 | - |  |  | SI | Posición: Suspensión ventral prono, una mano en el... |
| Q66 | - |  |  | SI | Presione y deslice un objeto romo a lo largo de la... |
| Q67 | - |  |  | SI | 15. Extensión de Cabeza y Cuello |
| Q68 | - |  |  | SI | Posición: Suspensión ventral prono, una mano en ab... |
| Q69 | - |  |  | SI | Presione y deslice un objeto romo sobre los paraes... |
| Q70 | - |  |  | SI | For infant over 10 kg knees and head may touch |
| Q71 | - |  |  | SI | 16. Extensión de Cabeza y Cuello Derecha |
| Q72 | - |  |  | SI | 16. Extensión de Cabeza y Cuello Izquierda |
| Q73 | - |  |  | SI | Total score |
| Q74 | - |  |  | SI | Score interpretation |
| Q75 | - |  |  | SI | * Adapted from the Test of Infant Motor Performanc... |
| Q76 | - |  |  | SI | Lower scores correspond to higher levels of disabi... |
| Q77 | - |  |  | SI | 0 - 64 |
| Q78 | - |  |  | SI | 0 - 64: Lower scores correspond to higher levels o... |
| Q79 | - |  |  | SI | The Children’s Hospital of Philadelphia Infant Tes... |
| Q80 | - |  |  | SI | Fecha |
| Q81 | - |  |  | SI | Hora |
| Q82 | - |  |  | SI | Score |
| Q83 | - |  |  | SI | Classification |
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