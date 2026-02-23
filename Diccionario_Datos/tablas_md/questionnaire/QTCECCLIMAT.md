# questionnaire.QTCECCLIMAT

> Control Climaterio

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Control Climaterio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Edad Menarquia (años) |
| Q02 | numeric |  |  | SI | Edad de Menopausia (años) |
| Q03 | numeric |  |  | SI | Tiempo de Menopausia (años) |
| Q04 | numeric |  |  | SI | Tiempo de Menopausia (meses) |
| Q05 | numeric |  |  | SI | Tiempo de Menopausia (dias) |
| Q06 | varchar |  |  | SI | Tipo de Menopausia |
| Q06A | varchar |  |  | SI | Menopausia Quirúrgica |
| Q07 | varchar |  |  | SI | Menopausia Quirúrgica |
| Q08 | numeric |  |  | SI | N° de Gestas |
| Q09 | numeric |  |  | SI | N° Partos |
| Q10 | numeric |  |  | SI | N° Abortos |
| Q11 | varchar |  |  | SI | Consumo Cigarrillos |
| Q12 | numeric |  |  | SI | N° Cigarrillos (Paquetes por Año) |
| Q13 | varchar |  |  | SI | Actividad Física |
| Q14 | varchar |  |  | SI | Actividad Sexual |
| Q15 | varchar |  |  | SI | Antecedentes de Fracturas |
| Q16 | varchar |  |  | SI | Falla Ovárica Prematura |
| Q17 | varchar |  |  | SI | Peso (Kg) |
| Q17ObsDR | varchar |  | FK | SI | Peso (Kg) DR |
| Q18 | varchar |  |  | SI | Talla (Cms) |
| Q18ObsDR | varchar |  | FK | SI | Talla (Cms) DR |
| Q19 | varchar |  |  | SI | Indice Masa Corporal |
| Q19ObsDR | varchar |  | FK | SI | Indice Masa Corporal DR |
| Q20 | varchar |  |  | SI | Circunferencia Cintura |
| Q20ObsDR | varchar |  | FK | SI | Circunferencia Cintura DR |
| Q21 | varchar |  |  | SI | Estado Nutricional |
| Q21ObsDR | varchar |  | FK | SI | Estado Nutricional DR |
| Q22 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q22ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q23 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q23ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q24 | varchar |  |  | SI | Resultado examen físico de Mamas |
| Q24ObsDR | varchar |  | FK | SI | Resultado examen físico de Mamas DR |
| Q25 | varchar |  |  | SI | Varices |
| Q26 | varchar |  |  | SI | Genitales externo |
| Q27 | varchar |  |  | SI | Vulva |
| Q28 | varchar |  |  | SI | Vagina |
| Q29 | varchar |  |  | SI | Cuello uterino |
| Q30 | varchar |  |  | SI | Cuerpo uterino |
| Q31 | varchar |  |  | SI | Anexos |
| Q49 | varchar |  |  | SI | Trombosis activa o estados protombóticos |
| Q50 | varchar |  |  | SI | Enfermedad coronaria |
| Q51 | varchar |  |  | SI | Accidente Vascular |
| Q52 | varchar |  |  | SI | Cáncer de Mama |
| Q53 | varchar |  |  | SI | Hiperplasia endometrial |
| Q54 | varchar |  |  | SI | Adenocarcinoma de endometrio |
| Q55 | varchar |  |  | SI | Adenocarcinoma de cuello uterino |
| Q56 | varchar |  |  | SI | Sangrado uterino de etiología no precisada |
| Q57 | varchar |  |  | SI | Insuficiencia hepática aguda |
| Q58 | varchar |  |  | SI | Indicación terapia hormonal |
| Q59 | date |  |  | SI | Fecha inicio terapia hormonal |
| Q60 | varchar |  |  | SI | Metodo prescrito |
| Q61 | varchar |  |  | SI | Otro Método prescrito |
| Q89 | varchar |  |  | SI | Tipo de Menopausia novo |
| Q90 | varchar |  |  | SI | Menopausia Quirúrgica  |
| QIMC | varchar |  |  | SI | IMC |
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