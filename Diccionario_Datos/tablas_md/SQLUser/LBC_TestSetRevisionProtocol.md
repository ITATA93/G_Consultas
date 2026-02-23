# SQLUser.LBC_TestSetRevisionProtocol

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRP_ParRef | bigint | PK |  | NO | - |
| LBCTSRP_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRP_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| LBCTSRP_Container_DR | bigint |  | FK | SI | Container |
| LBCTSRP_DateFrom | date |  |  | NO | Date From
Effective date for the record |
| LBCTSRP_DateTo | date |  |  | SI | Date To
Last day the record is active
Optional. ... |
| LBCTSRP_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRP_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRP_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRP_Protocol_DR | bigint |  | FK | NO | Lab Protocol |
| LBCTSRP_RowID | varchar |  |  | NO | - |
| LBCTSRP_Sequence | numeric |  |  | SI | Rule Sequence |
| LBCTSRP_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRP_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRP_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRP_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRP_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| Q01 | - |  |  | SI | Cereales |
| Q11 | - |  |  | SI | Verduras y Frutas |
| Q26 | - |  |  | SI | Carnes y Leguminosas |
| Q37 | - |  |  | SI | Aceites y Azúcares |
| Q60 | - |  |  | SI | Total Frutas |
| Q61 | - |  |  | SI | Encuesta de Consumo 24 horas |
| Q62 | - |  |  | SI | Total Azúcares |
| Q70 | - |  |  | SI | Total Cereales |
| QQ01 | - |  |  | SI | Total Verduras |
| QQ02 | - |  |  | SI | Arroz Frecuencia |
| QQ03 | - |  |  | SI | Arroz Porción |
| QQ05 | - |  |  | SI | Papas Frecuencia |
| QQ06 | - |  |  | SI | Papas Porción |
| QQ08 | - |  |  | SI | Pan Frecuencia |
| QQ09 | - |  |  | SI | Pan Porción |
| QQ12 | - |  |  | SI | Legumbres Frescas Frecuencia |
| QQ13 | - |  |  | SI | Legumbres Frescas Porción |
| QQ15 | - |  |  | SI | Lácteos |
| QQ16 | - |  |  | SI | Leche Frecuencia |
| QQ17 | - |  |  | SI | Leche Porción |
| QQ19 | - |  |  | SI | Leche Entera Frecuencia |
| QQ20 | - |  |  | SI | Leche Entera Porción |
| QQ22 | - |  |  | SI | Leche Semidescremada Frecuencia |
| QQ23 | - |  |  | SI | Leche Semidescremada Porción |
| QQ25 | - |  |  | SI | Leche Descremada Frecuencia |
| QQ26 | - |  |  | SI | Leche Descremada Porción |
| QQ27 | - |  |  | SI | Total Lácteos |
| QQ28 | - |  |  | SI | Quesos Frecuencia |
| QQ29 | - |  |  | SI | Quesos Porción |
| QQ30 | - |  |  | SI | Quesillo Frecuencia |
| QQ31 | - |  |  | SI | Quesillo Porción |
| QQ32 | - |  |  | SI | Legumbres Frecuencia |
| QQ33 | - |  |  | SI | Legumbres Porción |
| QQ34 | - |  |  | SI | Carnes Rojas Frecuencia |
| QQ35 | - |  |  | SI | Carnes Rojas Porción |
| QQ36 | - |  |  | SI | Huevos Frecuencia |
| QQ37 | - |  |  | SI | Huevos Porción |
| QQ38 | - |  |  | SI | Pescados Frecuencia |
| QQ39 | - |  |  | SI | Pescados Porción |
| QQ40 | - |  |  | SI | Aves Frecuencia |
| QQ41 | - |  |  | SI | Aves Porción |
| QQ42 | - |  |  | SI | Aceite Frecuencia |
| QQ43 | - |  |  | SI | Aceite Porción |
| QQ44 | - |  |  | SI | Palta - Aceitunas - Frutos Secos Frecuencia |
| QQ45 | - |  |  | SI | Palta - Aceitunas - Frutos Secos Porción |
| QQ46 | - |  |  | SI | Mantequilla - Margarina - Mayonesa Frecuencia |
| QQ47 | - |  |  | SI | Mantequilla - Margarina - Mayonesa Porción |
| QQ48 | - |  |  | SI | Manteca - Paté Frecuencia |
| QQ49 | - |  |  | SI | Manteca - Paté Porción |
| QQ50 | - |  |  | SI | Azúcar Frecuencia |
| QQ51 | - |  |  | SI | Azúcar Porción |
| QQ52 | - |  |  | SI | Miel - Mermelada Frecuencia |
| QQ53 | - |  |  | SI | Miel - Mermelada Porción |
| QQ54 | - |  |  | SI | Bebidas Azucaradas Frecuencia |
| QQ55 | - |  |  | SI | Bebidas Azucaradas Porción |
| QQ56 | - |  |  | SI | Verduras Frecuencia |
| QQ57 | - |  |  | SI | Verduras Porción |
| QQ58 | - |  |  | SI | Frutas Frecuencia |
| QQ59 | - |  |  | SI | Frutas Porción |
| QQ62 | - |  |  | SI | Total Carnes y Leguminosas |
| QQ63 | - |  |  | SI | Total Aceites |
| QQ80 | - |  |  | SI | Fideos Frecuencia |
| QQ82 | - |  |  | SI | Fideos Porcion |
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
| Qtestcalc | - |  |  | SI | Test Calculo |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*