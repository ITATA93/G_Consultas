# questionnaire.QTCECLACRI

> INGRESO UPC

**Schema:** questionnaire
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UPC

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | FECHA DE INGRESO |
| Q02 | time |  |  | SI | HORA DE INGRESO |
| Q03 | varchar |  |  | SI | PROCEDENCIA |
| Q04 | varchar |  |  | SI | INFORMACIÓN ENTREGADA POR |
| Q05 | varchar |  |  | SI | ANAMNESIS PRÓXIMA |
| Q06 | varchar |  |  | SI | DETALLE DEL CUESTINARIO |
| Q07 | varchar |  |  | SI | EXAMEN FÍSICO UNIFICADO |
| Q08 | varchar |  |  | SI | CHEQUEO ANTECEDENTES |
| Q09 | varchar |  |  | SI | CAPACIDAD FUNCIONAL |
| Q10 | varchar |  |  | SI | HÁBITOS |
| Q11 | varchar |  |  | SI | RESPIRATORIO |
| Q12 | varchar |  |  | SI | CARDIOVASCULAR |
| Q13 | varchar |  |  | SI | DIGESTIVO |
| Q14 | varchar |  |  | SI | HEMATOLOGIA/ONCOLOGIA |
| Q15 | varchar |  |  | SI | ENFERMEDADES INFECCIOSAS |
| Q16 | varchar |  |  | SI | DIABETES |
| Q17 | varchar |  |  | SI | ENDOCRINOLOGIA y NUTRICIÓN |
| Q18 | varchar |  |  | SI | CABEZA Y CUELLO |
| Q19 | varchar |  |  | SI | REUMATOLOGIA |
| Q20 | varchar |  |  | SI | NEUROLOGIA |
| Q21 | varchar |  |  | SI | PSIQUIATRÍA |
| Q22 | varchar |  |  | SI | GENITOURINARIO |
| Q23 | varchar |  |  | SI | MEDICAMENTOS DE USO RECIENTE |
| Q24 | varchar |  |  | SI | EXAMEN FÍSICO GENERAL |
| Q25 | varchar |  |  | SI | ACTITUD |
| Q26 | varchar |  |  | SI | PIEL Y MUCOSAS |
| Q27 | varchar |  |  | SI | RESPIRACIÓN |
| Q28 | varchar |  |  | SI | ABDOMEN |
| Q29 | varchar |  |  | SI | peso |
| Q29ObsDR | varchar |  | FK | SI | peso DR |
| Q30 | varchar |  |  | SI | talla |
| Q30ObsDR | varchar |  | FK | SI | talla DR |
| Q31 | varchar |  |  | SI | temperatura |
| Q31ObsDR | varchar |  | FK | SI | temperatura DR |
| Q32 | varchar |  |  | SI | frecuencia cardíaca |
| Q32ObsDR | varchar |  | FK | SI | frecuencia cardíaca DR |
| Q33 | varchar |  |  | SI | frecuencia respiratoria |
| Q33ObsDR | varchar |  | FK | SI | frecuencia respiratoria DR |
| Q34 | varchar |  |  | SI | presión arterial sistólica |
| Q34ObsDR | varchar |  | FK | SI | presión arterial sistólica DR |
| Q35 | varchar |  |  | SI | presión arterial diastólica |
| Q35ObsDR | varchar |  | FK | SI | presión arterial diastólica DR |
| Q36 | varchar |  |  | SI | presión arterial média |
| Q36ObsDR | varchar |  | FK | SI | presión arterial média DR |
| Q37 | varchar |  |  | SI | saturación oxígeno |
| Q37ObsDR | varchar |  | FK | SI | saturación oxígeno DR |
| Q38 | varchar |  |  | SI | EXAMEN FÍSICO GENERAL |
| Q39 | varchar |  |  | SI | EX. CABEZA Y CUELLO |
| Q40 | varchar |  |  | SI | CABEZA Y CUELLO |
| Q41 | varchar |  |  | SI | CABEZA Y CUELLO |
| Q42 | varchar |  |  | SI | EX. RESPIRATORIO |
| Q43 | varchar |  |  | SI | RESPIRATORIO |
| Q44 | varchar |  |  | SI | RESPIRATORIO |
| Q45 | varchar |  |  | SI | imagem |
| Q46 | varchar |  |  | SI | EX. CARDIOVASCULAR |
| Q47 | varchar |  |  | SI | NORMAL |
| Q48 | varchar |  |  | SI | ALTERACIONES DE RITMO |
| Q49 | varchar |  |  | SI | RUIDOS PATOLÓGICOS |
| Q50 | varchar |  |  | SI | CIRCULACIÓN CAPILAR |
| Q51 | varchar |  |  | SI | PULSOS PERIFÉRICOS DÉBILES O AUSENTES |
| Q52 | varchar |  |  | SI | EDEMA |
| Q53 | varchar |  |  | SI | CARDIOVASCULAR |
| Q54 | varchar |  |  | SI | EX. ABDOMEN |
| Q55 | varchar |  |  | SI | INSPECCIÓN |
| Q56 | varchar |  |  | SI | PALPACIÓN |
| Q57 | varchar |  |  | SI | VICEROMEGALIAS |
| Q58 | varchar |  |  | SI | CRUIDOS HIDROAÉREOS |
| Q59 | varchar |  |  | SI | CLOCALIZACIÓN DEL DOLOR |
| Q60 | varchar |  |  | SI | ABDOMEN |
| Q61 | varchar |  |  | SI | EX. NEUROLÓGICO |
| Q62 | varchar |  |  | SI | PUPILAS |
| Q63 | varchar |  |  | SI | HABLA |
| Q64 | varchar |  |  | SI | MOTOR |
| Q65 | varchar |  |  | SI | SENSIBILIDAD |
| Q66 | varchar |  |  | SI | REFLEJOS |
| Q67 | varchar |  |  | SI | SIGNOS MENÍNGEOS |
| Q68 | varchar |  |  | SI | NEUROLÓGICO |
| Q69 | varchar |  |  | SI | EX. GENITAL Y PELVIANO |
| Q70 | varchar |  |  | SI | GENITAL Y PELVIANO |
| Q71 | varchar |  |  | SI | EX. MÚSCULO ESQUELÉTICO |
| Q72 | varchar |  |  | SI | MÚSCULO ESQUELÉTICO |
| Q73 | varchar |  |  | SI | CONCLUSIÓN |
| Q74 | varchar |  |  | SI | CONCLUSIÓN |
| Q75 | varchar |  |  | SI | PLAN |
| Q76 | varchar |  |  | SI | PLAN |
| Q77 | varchar |  |  | SI | CHEQUEO DE ANTECEDENTES |
| Q78 | varchar |  |  | SI | EXAMENES DE LABORATORIO PERTINENTES |
| Q79 | varchar |  |  | SI | EXAMENES DE IMAGEN PERTINENTES |
| Q80 | varchar |  |  | SI | EXAMENES COMPLEMENTARIOS OTROS |
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