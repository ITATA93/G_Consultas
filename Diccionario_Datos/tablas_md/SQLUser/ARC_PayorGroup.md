# SQLUser.ARC_PayorGroup

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PGRP_RowId | bigint | PK |  | NO | - |
| PGRP_Code | varchar |  |  | NO | Code |
| PGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PGRP_CreatedDate | date |  |  | SI | Created Date |
| PGRP_CreatedTime | time |  |  | SI | Created Time |
| PGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PGRP_DateFrom | date |  |  | SI | Date From |
| PGRP_DateTo | date |  |  | SI | Date To |
| PGRP_Desc | varchar |  |  | NO | Description |
| PGRP_Owner | varchar |  |  | SI | Owner |
| PGRP_UpdatedDate | date |  |  | SI | Updated Date |
| PGRP_UpdatedTime | time |  |  | SI | Updated Time |
| PGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Datos Generales |
| Q02 | - |  |  | SI | Fecha Evaluación |
| Q03 | - |  |  | SI | Ubicación Paciente |
| Q04 | - |  |  | SI | Condición |
| Q05 | - |  |  | SI | Tiempo de Evolución |
| Q06 | - |  |  | SI | Lateralidad Manual |
| Q07 | - |  |  | SI | Escolaridad |
| Q08 | - |  |  | SI | Observación Escolaridad |
| Q09 | - |  |  | SI | Ocupación Pre-Mórbida |
| Q10 | - |  |  | SI | Red de Apoyo |
| Q11 | - |  |  | SI | Entrevista |
| Q12 | - |  |  | SI | Déficit Sensitivo/Motor |
| Q13 | - |  |  | SI | Hemiparesia (tipo) |
| Q14 | - |  |  | SI | Hemiparesia |
| Q15 | - |  |  | SI | Tetraparesia |
| Q16 | - |  |  | SI | Tetraplejia |
| Q17 | - |  |  | SI | Displejia |
| Q18 | - |  |  | SI | Normal |
| Q19 | - |  |  | SI | Compromiso de Conciencia |
| Q20 | - |  |  | SI | Orientación |
| Q21 | - |  |  | SI | Canales de Entrada |
| Q22 | - |  |  | SI | Canales Salida |
| Q23 | - |  |  | SI | Atención Focalizada |
| Q24 | - |  |  | SI | Atención Sostenida |
| Q25 | - |  |  | SI | Conducta Contextual |
| Q26 | - |  |  | SI | Memoria |
| Q27 | - |  |  | SI | Epilepsia (Crisis) |
| Q28 | - |  |  | SI | Frecuencia |
| Q29 | - |  |  | SI | Postura |
| Q30 | - |  |  | SI | Control de Cabeza |
| Q31 | - |  |  | SI | Control de Tronco |
| Q32 | - |  |  | SI | Control Sedente |
| Q33 | - |  |  | SI | Control Bípedo |
| Q34 | - |  |  | SI | Uso ATT |
| Q35 | - |  |  | SI | Observación |
| Q36 | - |  |  | SI | Funciones Laríngeas |
| Q37 | - |  |  | SI | Fonación Espontánea |
| Q38 | - |  |  | SI | Calidad de la voz |
| Q39 | - |  |  | SI | Funciones Protectoras |
| Q40 | - |  |  | SI | Carraspeo Voluntario |
| Q41 | - |  |  | SI | Tos Voluntaria |
| Q42 | - |  |  | SI | Tos Refleja |
| Q43 | - |  |  | SI | Activación de la Respuesta Motora Orofaríngea (RMO... |
| Q44 | - |  |  | SI | Evaluación No Nutritiva |
| Q45 | - |  |  | SI | Frecuencia Deglutoria Espontánea (FDE) |
| Q46 | - |  |  | SI | dgl/min |
| Q47 | - |  |  | SI | Prueba Deglución Repetitiva (PDR) |
| Q48 | - |  |  | SI | dgl/30 seg |
| Q49 | - |  |  | SI | Alimentación / Deglución |
| Q50 | - |  |  | SI | Vía Alimentación |
| Q51 | - |  |  | SI | Fórmula |
| Q52 | - |  |  | SI | Sólidos Modificados |
| Q53 | - |  |  | SI | Líquidos Modificados |
| Q54 | - |  |  | SI | Litros/día |
| Q55 | - |  |  | SI | Vía |
| Q56 | - |  |  | SI | Estado Nutricional |
| Q57 | - |  |  | SI | Cuánto se demora en recibir almuerzo/cena |
| Q58 | - |  |  | SI | minutos |
| Q59 | - |  |  | SI | Sialorrea |
| Q60 | - |  |  | SI | Xerostomía |
| Q61 | - |  |  | SI | EAT 10 |
| Q62 | - |  |  | SI | / 10 puntos |
| Q63 | - |  |  | SI | Comunicación |
| Q64 | - |  |  | SI | Lenguaje |
| Q65 | - |  |  | SI | Alteración de Inteligibilidad |
| Q66 | - |  |  | SI | Sistemas de Comunicación Aumentatitva – Alternativ... |
| Q67 | - |  |  | SI | Implementado |
| Q68 | - |  |  | SI | ¿Cuál? |
| Q69 | - |  |  | SI | Contexto |
| Q70 | - |  |  | SI | Otros |
| Q71 | - |  |  | SI | Plan de Evaluación |
| Q72 | - |  |  | SI | Plan de Evaluación |
| Q73 | - |  |  | SI | Observaciones Plan de Evaluación |
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