# questionnaire.QTCEPANSS

> Escala de Síndromes Positivo y Negativo (PANSS)

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Síndromes Positivo y Negativo (PANSS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | P1 Delirios |
| Q02 | numeric |  |  | SI | P2 Desorganización conceptual |
| Q03 | numeric |  |  | SI | P3 Comportamiento alucinatorio |
| Q04 | numeric |  |  | SI | P4  |
| Q05 | numeric |  |  | SI | P5 Grandiosidad |
| Q06 | numeric |  |  | SI | P6 Suspicacia/persecución |
| Q07 | numeric |  |  | SI | P7 Hostilidad |
| Q08 | varchar |  |  | SI | Subtotal Sub Escala Positiva |
| Q09 | numeric |  |  | SI | N1 Embotamiento afectivo |
| Q10 | numeric |  |  | SI | N2 Retracción emocional |
| Q11 | numeric |  |  | SI | N3 Pobre relación |
| Q12 | numeric |  |  | SI | N4 Retracción social, apatía pasiva |
| Q13 | numeric |  |  | SI | N5 Dificultad de pensamiento abstracto |
| Q14 | numeric |  |  | SI | N6 Falta de espontaneidad y fluidez de la conversa... |
| Q15 | numeric |  |  | SI | N7 Pensamiento estereotipado |
| Q16 | varchar |  |  | SI | Subtotal Sub Escala Negativa |
| Q17 | numeric |  |  | SI | G1 Preocupaciones somáticas |
| Q18 | numeric |  |  | SI | G2 Ansiedad |
| Q19 | numeric |  |  | SI | G3 Sentimiento de culpa |
| Q20 | numeric |  |  | SI | G4 Tensión motora |
| Q21 | numeric |  |  | SI | G5 Manierismos y postura |
| Q22 | numeric |  |  | SI | G6 Depresión |
| Q23 | numeric |  |  | SI | G7 Retardo motor |
| Q24 | numeric |  |  | SI | G8 Falta de colaboración |
| Q25 | numeric |  |  | SI | G9 Inusuales contenidos del pensamiento |
| Q26 | numeric |  |  | SI | G10 Desorientación |
| Q27 | numeric |  |  | SI | G11 Atención deficiente |
| Q28 | numeric |  |  | SI | G12 Ausencia de juicio e introspección |
| Q29 | numeric |  |  | SI | G13 Trastorno de la volición |
| Q30 | numeric |  |  | SI | G13 Control deficiente de impulsos |
| Q31 | numeric |  |  | SI | G14 Control deficiente de impulsos |
| Q32 | numeric |  |  | SI | G15 Preocupación |
| Q33 | numeric |  |  | SI | G16 Evitación social activa |
| Q34 | varchar |  |  | SI | Subtotal Sub Escala Psicopatología General |
| Q35 | varchar |  |  | SI | Puntaje Total PANSS |
| Q36 | varchar |  |  | SI | Sub Escala Positiva |
| Q37 | varchar |  |  | SI | Sub Escala Negativa |
| Q38 | varchar |  |  | SI | Sub Escala Psicopatología General |
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