# questionnaire.QCLXXDOSS

> Escala Severidad de la Disfagia (DOSS)

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala Severidad de la Disfagia (DOSS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Escala de Severidad |
| Q02 | varchar |  |  | SI | El paciente presenta o puede presentar alguna de e... |
| Q03 | varchar |  |  | SI | Nivel 7 (N7) |
| Q04 | varchar |  |  | SI | - Deglución normal en todos los casos |
| Q05 | varchar |  |  | SI | Nivel 6 (N6) |
| Q06 | varchar |  |  | SI | - Leve atraso oral o faríngeo, estancamiento o res... |
| Q07 | varchar |  |  | SI | - Puede necesitar de tiempo extra para las comidas... |
| Q08 | varchar |  |  | SI | Nivel 5 (N5) |
| Q09 | varchar |  |  | SI | - Aspiración solamente de líquidos, pero con un fu... |
| Q10 | varchar |  |  | SI | - Penetración sobre los pliegues vocales con una o... |
| Q11 | varchar |  |  | SI | - Estancamiento en la faringe, y que despeja espon... |
| Q12 | varchar |  |  | SI | Nivel 4 (N4) |
| Q13 | varchar |  |  | SI | - Estancamiento en la faringe, despeja con orienta... |
| Q14 | varchar |  |  | SI | - Aspiración con una consistencia, con reflejo de ... |
| Q15 | varchar |  |  | SI | - La penetración a nivel de los pliegues vocales c... |
| Q16 | varchar |  |  | SI | - La penetración a nivel de los pliegues vocales s... |
| Q17 | varchar |  |  | SI | Nivel 3 (N3) |
| Q18 | varchar |  |  | SI | - Estancamiento moderado de la faringe, despeje co... |
| Q19 | varchar |  |  | SI | - Estancamiento moderado en la cavidad oral, despe... |
| Q20 | varchar |  |  | SI | - Nivel de penetración en los pliegues vocales sin... |
| Q21 | varchar |  |  | SI | - Aspiración de dos consistencias, con reflejo de ... |
| Q22 | varchar |  |  | SI | - Aspiración de una consistencia, sin tos ni penet... |
| Q23 | varchar |  |  | SI | Nivel 2 (N2) |
| Q24 | varchar |  |  | SI | - Estancamiento grave en la faringe, incapacidad d... |
| Q25 | varchar |  |  | SI | - Estancamiento grave o pérdida del bolo en fase o... |
| Q26 | varchar |  |  | SI | - Aspiración con dos o más consistencias, sin refl... |
| Q27 | varchar |  |  | SI | Nivel 1 (N1) |
| Q28 | varchar |  |  | SI | - Estancamiento severo en la faringe, siendo incap... |
| Q29 | varchar |  |  | SI | - Estancamiento o pérdida de bolo en forma oral se... |
| Q30 | varchar |  |  | SI | - Aspiración silenciosa con dos o más consistencia... |
| Q31 | varchar |  |  | SI | VÍA ORAL SUSPENDIDA - NECESIDAD DE NUTRICÓN NO ORA... |
| Q32 | varchar |  |  | SI | VÍA ORAL SUSPENDIDA - NECESIDAD DE NUTRICÓN NO ORA... |
| Q33 | varchar |  |  | SI | Máxima asistencia de uso de estrategias con vía or... |
| Q34 | varchar |  |  | SI | DIETA POR VÍA ORAL MODIFICADA Y/O INDEPENDIENTE.&n... |
| Q35 | varchar |  |  | SI | Total asistencia, supervisión o estrategia, restri... |
| Q36 | varchar |  |  | SI | DIETA POR VÍA ORAL MODIFICADA Y/O INDEPENDIENTE. |
| Q37 | varchar |  |  | SI | Supervisión a distancia, puede necesitar de restri... |
| Q38 | varchar |  |  | SI | DIETA NORMAL POR VÏA ORAL. |
| Q39 | varchar |  |  | SI | Ninguna estrategia o tiempo extra necesario |
| Q40 | varchar |  |  | SI | DIETA POR VÍA ORAL MODIFICADA Y/O INDEPENDIENTE. |
| Q41 | varchar |  |  | SI | Supervisión a distancia, puede necesitar de restri... |
| Q42 | varchar |  |  | SI | DIETA NORMAL POR VÏA ORAL. |
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