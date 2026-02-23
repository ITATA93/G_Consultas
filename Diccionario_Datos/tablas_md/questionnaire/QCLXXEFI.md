# questionnaire.QCLXXEFI

> Evaluación Fonoaudiológica Inicial para Adultos (EFI)

**Schema:** questionnaire
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Fonoaudiológica Inicial para Adultos (EFI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Datos Generales |
| Q02 | date |  |  | SI | Fecha Evaluación |
| Q03 | varchar |  |  | SI | Ubicación Paciente |
| Q04 | varchar |  |  | SI | Condición |
| Q05 | varchar |  |  | SI | Tiempo de Evolución |
| Q06 | varchar |  |  | SI | Lateralidad Manual |
| Q07 | varchar |  |  | SI | Escolaridad |
| Q08 | varchar |  |  | SI | Observación Escolaridad |
| Q09 | varchar |  |  | SI | Ocupación Pre-Mórbida |
| Q10 | varchar |  |  | SI | Red de Apoyo |
| Q11 | varchar |  |  | SI | Entrevista |
| Q12 | varchar |  |  | SI | Déficit Sensitivo/Motor |
| Q13 | varchar |  |  | SI | Hemiparesia (tipo) |
| Q14 | varchar |  |  | SI | Hemiparesia |
| Q15 | varchar |  |  | SI | Tetraparesia |
| Q16 | varchar |  |  | SI | Tetraplejia |
| Q17 | varchar |  |  | SI | Displejia |
| Q18 | varchar |  |  | SI | Normal |
| Q19 | varchar |  |  | SI | Compromiso de Conciencia |
| Q20 | varchar |  |  | SI | Orientación |
| Q21 | varchar |  |  | SI | Canales de Entrada |
| Q22 | varchar |  |  | SI | Canales Salida |
| Q23 | varchar |  |  | SI | Atención Focalizada |
| Q24 | varchar |  |  | SI | Atención Sostenida |
| Q25 | varchar |  |  | SI | Conducta Contextual |
| Q26 | varchar |  |  | SI | Memoria |
| Q27 | varchar |  |  | SI | Epilepsia (Crisis) |
| Q28 | numeric |  |  | SI | Frecuencia |
| Q29 | varchar |  |  | SI | Postura |
| Q30 | varchar |  |  | SI | Control de Cabeza |
| Q31 | varchar |  |  | SI | Control de Tronco |
| Q32 | varchar |  |  | SI | Control Sedente |
| Q33 | varchar |  |  | SI | Control Bípedo |
| Q34 | varchar |  |  | SI | Uso ATT |
| Q35 | varchar |  |  | SI | Observación |
| Q36 | varchar |  |  | SI | Funciones Laríngeas |
| Q37 | varchar |  |  | SI | Fonación Espontánea |
| Q38 | varchar |  |  | SI | Calidad de la voz |
| Q39 | varchar |  |  | SI | Funciones Protectoras |
| Q40 | varchar |  |  | SI | Carraspeo Voluntario |
| Q41 | varchar |  |  | SI | Tos Voluntaria |
| Q42 | varchar |  |  | SI | Tos Refleja |
| Q43 | varchar |  |  | SI | Activación de la Respuesta Motora Orofaríngea (RMO... |
| Q44 | varchar |  |  | SI | Evaluación No Nutritiva |
| Q45 | numeric |  |  | SI | Frecuencia Deglutoria Espontánea (FDE) |
| Q46 | varchar |  |  | SI | dgl/min |
| Q47 | numeric |  |  | SI | Prueba Deglución Repetitiva (PDR) |
| Q48 | varchar |  |  | SI | dgl/30 seg |
| Q49 | varchar |  |  | SI | Alimentación / Deglución |
| Q50 | varchar |  |  | SI | Vía Alimentación |
| Q51 | varchar |  |  | SI | Fórmula |
| Q52 | varchar |  |  | SI | Sólidos Modificados |
| Q53 | varchar |  |  | SI | Líquidos Modificados |
| Q54 | numeric |  |  | SI | Litros/día |
| Q55 | varchar |  |  | SI | Vía |
| Q56 | varchar |  |  | SI | Estado Nutricional |
| Q57 | numeric |  |  | SI | Cuánto se demora en recibir almuerzo/cena |
| Q58 | varchar |  |  | SI | minutos |
| Q59 | varchar |  |  | SI | Sialorrea |
| Q60 | varchar |  |  | SI | Xerostomía |
| Q61 | numeric |  |  | SI | EAT 10 |
| Q62 | varchar |  |  | SI | / 10 puntos |
| Q63 | varchar |  |  | SI | Comunicación |
| Q64 | varchar |  |  | SI | Lenguaje |
| Q65 | varchar |  |  | SI | Alteración de Inteligibilidad |
| Q66 | varchar |  |  | SI | Sistemas de Comunicación Aumentatitva – Alternativ... |
| Q67 | varchar |  |  | SI | Implementado |
| Q68 | varchar |  |  | SI | ¿Cuál? |
| Q69 | varchar |  |  | SI | Contexto |
| Q70 | varchar |  |  | SI | Otros |
| Q71 | varchar |  |  | SI | Plan de Evaluación |
| Q72 | varchar |  |  | SI | Plan de Evaluación |
| Q73 | varchar |  |  | SI | Observaciones Plan de Evaluación |
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