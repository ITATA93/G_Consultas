# questionnaire.QCLXXEMPMC

> Examen Medicina Preventiva Modificado - Climaterio

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Medicina Preventiva Modificado - Climaterio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | fecha de vigencia EMPA |
| Q02 | varchar |  |  | SI | Audit |
| Q03 | varchar |  |  | SI | Realiza ejercicio |
| Q04 | varchar |  |  | SI | Fumador |
| Q05 | varchar |  |  | SI | Se ha sentido triste, deprimida o pesimista casi t... |
| Q06 | varchar |  |  | SI | Siente que ya no disfruta o ha perdido el interés  |
| Q07 | varchar |  |  | SI | ¿Duran los síntomas más de dos semanas?  |
| Q08 | varchar |  |  | SI | Peso |
| Q08ObsDR | varchar |  | FK | SI | Peso DR |
| Q09 | varchar |  |  | SI | Talla |
| Q09ObsDR | varchar |  | FK | SI | Talla DR |
| Q10 | varchar |  |  | SI | IMC |
| Q11 | varchar |  |  | SI | Circunferencia cintura |
| Q11ObsDR | varchar |  | FK | SI | Circunferencia cintura DR |
| Q12 | numeric |  |  | SI | Talla Máxima Registrada |
| Q13 | varchar |  |  | SI | Pérdida de Estatura > 7 cm  |
| Q14 | varchar |  |  | SI | Estado Nutricional  |
| Q14ObsDR | varchar |  | FK | SI | Estado Nutricional  DR |
| Q15 | varchar |  |  | SI | Presión Arterial Sistólica Actual  |
| Q15ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica Actual  DR |
| Q16 | varchar |  |  | SI | Presión Arterial Diastólica Actual  |
| Q16ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica Actual  DR |
| Q17 | varchar |  |  | SI | Colesterol Total Actual |
| Q17ObsDR | varchar |  | FK | SI | Colesterol Total Actual DR |
| Q18 | varchar |  |  | SI | Colesterol HDL Actual |
| Q18ObsDR | varchar |  | FK | SI | Colesterol HDL Actual DR |
| Q19 | varchar |  |  | SI | Triglicéridos Actual  |
| Q19ObsDR | varchar |  | FK | SI | Triglicéridos Actual  DR |
| Q20 | varchar |  |  | SI | Glicemia Actual  |
| Q20ObsDR | varchar |  | FK | SI | Glicemia Actual  DR |
| Q21 | varchar |  |  | SI | Riesgo Cardiovascular ATP III |
| Q22 | varchar |  |  | SI | Ha tenido tos productiva por más de 15 días  |
| Q23 | varchar |  |  | SI | V.D.R.L |
| Q23ObsDR | varchar |  | FK | SI | V.D.R.L DR |
| Q24 | varchar |  |  | SI | R.P.R |
| Q24ObsDR | varchar |  | FK | SI | R.P.R DR |
| Q25 | varchar |  |  | SI | Requiere VIH |
| Q26 | varchar |  |  | SI | Prevención de cáncer cérvico-uterino  |
| Q27 | varchar |  |  | SI | Fecha examen |
| Q28 | varchar |  |  | SI | Diagnóstico Primario |
| Q29 | varchar |  |  | SI | Descripción de calidad de la muestra |
| Q30 | varchar |  |  | SI | Diagnósticos Secundarios |
| Q31 | varchar |  |  | SI | Descripción de Sugerencias |
| Q32 | varchar |  |  | SI | Fecha Próximo PAP  |
| Q33 | varchar |  |  | SI | Mamografía  |
| Q34 | varchar |  |  | SI | Fecha de registro mamografía  |
| Q35 | varchar |  |  | SI | Mamografía |
| Q36 | varchar |  |  | SI | Conducta a seguir  |
| Q37 | varchar |  |  | SI | Fecha de próxima mamografía  |
| Q38 | varchar |  |  | SI | Observaciones  |
| Q39 | varchar |  |  | SI | Plan  |
| Q40 | varchar |  |  | SI | Estado del EMPA |
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