# questionnaire.QCLXXESCFIM

> Escala FIM (TM)

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala FIM (TM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | A. Alimentación |
| Q02 | varchar |  |  | SI | B. Aseo Menor |
| Q03 | varchar |  |  | SI | C. Aseo Mayor |
| Q04 | varchar |  |  | SI | D. Vestuario Cuerpo Superior |
| Q05 | varchar |  |  | SI | E. Vestuario Cuerpo Inferior |
| Q06 | varchar |  |  | SI | F. Aseo Perineal |
| Q07 | varchar |  |  | SI | G. Manejo Vesical |
| Q08 | varchar |  |  | SI | H. Manejo Intestinal |
| Q09 | varchar |  |  | SI | I. Cama - Silla |
| Q10 | varchar |  |  | SI | J. WC |
| Q11 | varchar |  |  | SI | K. Tina o Ducha |
| Q12 | varchar |  |  | SI | L. Marcha/Silla de Ruedas |
| Q13 | varchar |  |  | SI | M. Escalas |
| Q14 | varchar |  |  | SI | N. Comprensión |
| Q15 | varchar |  |  | SI | O. Expresión |
| Q16 | varchar |  |  | SI | P. Interacción Social |
| Q17 | varchar |  |  | SI | Q. Solución de Problemas |
| Q18 | varchar |  |  | SI | R. Memoria |
| Q19 | varchar |  |  | SI | Autocuidado |
| Q20 | varchar |  |  | SI | Control Esfinteriano |
| Q21 | varchar |  |  | SI | Transferencias |
| Q22 | varchar |  |  | SI | Locomoción |
| Q23 | varchar |  |  | SI | Comunicación |
| Q24 | varchar |  |  | SI | Cognición Social |
| Q25 | varchar |  |  | SI | Motor |
| Q26 | varchar |  |  | SI | Cognitivo |
| Q27 | varchar |  |  | SI | Resultado Escala de FIM |
| Q27ObsDR | varchar |  | FK | SI | Resultado Escala de FIM DR |
| Q28 | varchar |  |  | SI | Autocuidado |
| Q29 | varchar |  |  | SI | Control Esfinteriano |
| Q30 | varchar |  |  | SI | Transferencias |
| Q31 | varchar |  |  | SI | Locomoción |
| Q32 | varchar |  |  | SI | Comunicación |
| Q33 | varchar |  |  | SI | Cognición Social |
| Q34 | varchar |  |  | SI | SUB - ESCALAS |
| Q35 | varchar |  |  | SI | DOMINIO |
| Q36 | varchar |  |  | SI | GRADO DE DEPENDENCIA   |
| Q37 | varchar |  |  | SI | Sin Ayuda |
| Q38 | varchar |  |  | SI | Dependencia Modificada |
| Q39 | varchar |  |  | SI | Dependencia Completa |
| Q40 | varchar |  |  | SI | NIVEL DE FUNCIONALIDAD   |
| Q41 | varchar |  |  | SI | 7. Independencia completa |
| Q42 | varchar |  |  | SI | 6. Independencia modificada |
| Q43 | varchar |  |  | SI | 5. Supervisión |
| Q44 | varchar |  |  | SI | 4. Asistencia mínima (mayor 75% independencia) |
| Q45 | varchar |  |  | SI | 3. Asistencia moderada (mayor 50% independencia) |
| Q46 | varchar |  |  | SI | 2. Asistencia máxima (mayor 25% independencia) |
| Q47 | varchar |  |  | SI | 1. Asistencia total (menor 25% independencia) |
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