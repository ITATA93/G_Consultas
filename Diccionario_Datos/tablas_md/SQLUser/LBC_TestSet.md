# SQLUser.LBC_TestSet

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTS_RowID | bigint | PK |  | NO | - |
| LBCTS_Code | varchar |  |  | NO | Code |
| LBCTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTS_DateFrom | date |  |  | SI | Date From |
| LBCTS_DateTo | date |  |  | SI | Date To |
| LBCTS_Department_DR | bigint |  | FK | NO | Department
The department the test set belongs to... |
| LBCTS_Desc | varchar |  |  | SI | Description
The description is based on the curre... |
| LBCTS_Owner | varchar |  |  | SI | Owner |
| Q01 | - |  |  | SI | P1 Delirios |
| Q02 | - |  |  | SI | P2 Desorganización conceptual |
| Q03 | - |  |  | SI | P3 Comportamiento alucinatorio |
| Q04 | - |  |  | SI | P4 |
| Q05 | - |  |  | SI | P5 Grandiosidad |
| Q06 | - |  |  | SI | P6 Suspicacia/persecución |
| Q07 | - |  |  | SI | P7 Hostilidad |
| Q08 | - |  |  | SI | Subtotal Sub Escala Positiva |
| Q09 | - |  |  | SI | N1 Embotamiento afectivo |
| Q10 | - |  |  | SI | N2 Retracción emocional |
| Q11 | - |  |  | SI | N3 Pobre relación |
| Q12 | - |  |  | SI | N4 Retracción social, apatía pasiva |
| Q13 | - |  |  | SI | N5 Dificultad de pensamiento abstracto |
| Q14 | - |  |  | SI | N6 Falta de espontaneidad y fluidez de la conversa... |
| Q15 | - |  |  | SI | N7 Pensamiento estereotipado |
| Q16 | - |  |  | SI | Subtotal Sub Escala Negativa |
| Q17 | - |  |  | SI | G1 Preocupaciones somáticas |
| Q18 | - |  |  | SI | G2 Ansiedad |
| Q19 | - |  |  | SI | G3 Sentimiento de culpa |
| Q20 | - |  |  | SI | G4 Tensión motora |
| Q21 | - |  |  | SI | G5 Manierismos y postura |
| Q22 | - |  |  | SI | G6 Depresión |
| Q23 | - |  |  | SI | G7 Retardo motor |
| Q24 | - |  |  | SI | G8 Falta de colaboración |
| Q25 | - |  |  | SI | G9 Inusuales contenidos del pensamiento |
| Q26 | - |  |  | SI | G10 Desorientación |
| Q27 | - |  |  | SI | G11 Atención deficiente |
| Q28 | - |  |  | SI | G12 Ausencia de juicio e introspección |
| Q29 | - |  |  | SI | G13 Trastorno de la volición |
| Q30 | - |  |  | SI | G13 Control deficiente de impulsos |
| Q31 | - |  |  | SI | G14 Control deficiente de impulsos |
| Q32 | - |  |  | SI | G15 Preocupación |
| Q33 | - |  |  | SI | G16 Evitación social activa |
| Q34 | - |  |  | SI | Subtotal Sub Escala Psicopatología General |
| Q35 | - |  |  | SI | Puntaje Total PANSS |
| Q36 | - |  |  | SI | Sub Escala Positiva |
| Q37 | - |  |  | SI | Sub Escala Negativa |
| Q38 | - |  |  | SI | Sub Escala Psicopatología General |
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