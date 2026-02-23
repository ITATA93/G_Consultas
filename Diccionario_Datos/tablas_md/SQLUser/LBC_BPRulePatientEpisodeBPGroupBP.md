# SQLUser.LBC_BPRulePatientEpisodeBPGroupBP

**Schema:** SQLUser
**Columnas:** 151
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPRPEBPGBP_ParRef | varchar | PK |  | NO | Parent Blood-Product Rule Blood Product Group Deta... |
| LBCBPRPEBPGBP_AntigenReaction | varchar |  |  | SI | Antigen Reaction |
| LBCBPRPEBPGBP_Antigen_DR | bigint |  | FK | SI | Antigen |
| LBCBPRPEBPGBP_BloodGroup_DR | bigint |  | FK | SI | Blood Group |
| LBCBPRPEBPGBP_BloodProduct_DR | bigint |  | FK | SI | Blood Product |
| LBCBPRPEBPGBP_CMVStatus | varchar |  |  | SI | CMV Status |
| LBCBPRPEBPGBP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBPRPEBPGBP_DateTo | date |  |  | SI | Last day the record is active |
| LBCBPRPEBPGBP_Desc | varchar |  |  | NO | Description |
| LBCBPRPEBPGBP_EntryMode_DR | bigint |  | FK | SI | Mode of Entry |
| LBCBPRPEBPGBP_FullDesc | longvarchar |  |  | SI | Full Description
HTMLRichText |
| LBCBPRPEBPGBP_HbSStatus | varchar |  |  | SI | HbS Status |
| LBCBPRPEBPGBP_HepatitisE | varchar |  |  | SI | Hepatitis E |
| LBCBPRPEBPGBP_HighTitreHaemolysinsStatus | varchar |  |  | SI | High Titre Haemolysins Status |
| LBCBPRPEBPGBP_IrradiatedStatus | varchar |  |  | SI | Irradiated Status |
| LBCBPRPEBPGBP_Message | varchar |  |  | NO | Message |
| LBCBPRPEBPGBP_NotAntigen | varchar |  |  | SI | Not Antigen
Logically negate the selected Antigen... |
| LBCBPRPEBPGBP_NotCMVStatus | varchar |  |  | SI | Not CMV Status
Logically negate the selected CMV ... |
| LBCBPRPEBPGBP_NotHbSStatus | varchar |  |  | SI | Not HbS Status
Logically negate the selected HbS ... |
| LBCBPRPEBPGBP_NotHepatitisE | varchar |  |  | SI | Not Hepatitis E
Logically negate the selected Hep... |
| LBCBPRPEBPGBP_RowID | varchar |  |  | NO | - |
| LBCBPRPEBPGBP_RuleAction | varchar |  |  | NO | Rule Action |
| LBCBPRPEBPGBP_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCBPRPEBPGBP_UnitAgeFrom | double |  |  | SI | Age of Unit From |
| LBCBPRPEBPGBP_UnitAgeFromUOM | varchar |  |  | SI | Age of Unit From UOM |
| LBCBPRPEBPGBP_UnitAgeTo | double |  |  | SI | Age of Unit To |
| LBCBPRPEBPGBP_UnitAgeToUOM | varchar |  |  | SI | Age of Unit To UOM |
| Q01 | - |  |  | SI | Peso al Nacer |
| Q02 | - |  |  | SI | Talla al Nacer |
| Q03 | - |  |  | SI | Edad Gestacional (Semanas) |
| Q04 | - |  |  | SI | APGAR 1 |
| Q05 | - |  |  | SI | APGAR 3 |
| Q06 | - |  |  | SI | APGAR 5 |
| Q07 | - |  |  | SI | APGAR 10 |
| Q08 | - |  |  | SI | Perimetro Cefalico |
| Q09 | - |  |  | SI | Reanimación Respiratoria |
| Q10 | - |  |  | SI | Patología de Recien Nacido |
| Q11 | - |  |  | SI | Patología durante el embarazo |
| Q12 | - |  |  | SI | Detalle de Patología durante el Embarazo |
| Q13 | - |  |  | SI | Especificación otras patologías durante el embaraz... |
| Q14 | - |  |  | SI | Tipo de Parto |
| Q15 | - |  |  | SI | Resultado de Score de riesgo de Morir por Broncone... |
| Q16 | - |  |  | SI | 1.- Fecha Hospitalización |
| Q17 | - |  |  | SI | 1.- Edad Hospitalización |
| Q18 | - |  |  | SI | 1.- Diagnóstico/Causa |
| Q19 | - |  |  | SI | 2.- Fecha Hospitalización |
| Q20 | - |  |  | SI | 2.- Edad Hospitalización |
| Q21 | - |  |  | SI | 2.- Diagnóstico/Causa |
| Q22 | - |  |  | SI | 3.- Fecha Hospitalización |
| Q23 | - |  |  | SI | 3.- Edad Hospitalización |
| Q24 | - |  |  | SI | 3.- Diagnóstico/Causa |
| Q25 | - |  |  | SI | 4.- Fecha Hospitalización |
| Q26 | - |  |  | SI | 4.- Edad Hospitalización |
| Q27 | - |  |  | SI | 4.- Diagnóstico/Causa |
| Q28 | - |  |  | SI | 1.- Fecha IC |
| Q29 | - |  |  | SI | 1.- Especialidad IC |
| Q30 | - |  |  | SI | 1.- Motivo IC |
| Q31 | - |  |  | SI | 2.- Fecha IC |
| Q32 | - |  |  | SI | 2.- Especialidad IC |
| Q33 | - |  |  | SI | 2.- Motivo IC |
| Q34 | - |  |  | SI | 3.- Fecha IC |
| Q35 | - |  |  | SI | 3.- Especialidad IC |
| Q36 | - |  |  | SI | 3.- Motivo IC |
| Q37 | - |  |  | SI | 4.- Fecha IC |
| Q38 | - |  |  | SI | 4.- Especialidad IC |
| Q39 | - |  |  | SI | 4.- Motivo IC |
| Q40 | - |  |  | SI | Control por |
| Q41 | - |  |  | SI | Diagnóstico |
| Q42 | - |  |  | SI | Evaluación Control |
| Q43 | - |  |  | SI | PEF (%) |
| Q44 | - |  |  | SI | Indicaciones |
| Q45 | - |  |  | SI | Inhaladores de Mantención |
| Q46 | - |  |  | SI | Medicamentos |
| Q47 | - |  |  | SI | SCI (Score de Ingreso) |
| Q48 | - |  |  | SI | SCE (Score de Egreso) |
| Q49 | - |  |  | SI | Resultado RX Tórax |
| Q50 | - |  |  | SI | Detalle Resultado RX Tórax |
| Q51 | - |  |  | SI | Fecha Resultado RX Tórax |
| Q52 | - |  |  | SI | Resultado Flujometría |
| Q53 | - |  |  | SI | Detalle Resultado Flujometría |
| Q54 | - |  |  | SI | Fecha Resultado Flujometría |
| Q55 | - |  |  | SI | Resultado Espirometría |
| Q56 | - |  |  | SI | Detalle Resultado Espirometría |
| Q57 | - |  |  | SI | Fecha Resultado Espirometría |
| Q58 | - |  |  | SI | Resultado Test de Ejercicios |
| Q59 | - |  |  | SI | Detalle Resultado Test de Ejercicios |
| Q60 | - |  |  | SI | Fecha Resultado Test de Ejercicios |
| Q61 | - |  |  | SI | Resultado Eosinofilos |
| Q62 | - |  |  | SI | Detalle Resultado Eosinofilos |
| Q63 | - |  |  | SI | Fecha Resultado Eosinofilos |
| Q64 | - |  |  | SI | Resultado Test Cutáneo |
| Q65 | - |  |  | SI | Detalle Resultado Test Cutáneo |
| Q66 | - |  |  | SI | Fecha Resultado Test Cutáneo |
| Q67 | - |  |  | SI | Resultado Test del Sudor |
| Q68 | - |  |  | SI | Detalle Resultado Test del Sudor |
| Q69 | - |  |  | SI | Fecha Resultado Test del Sudor |
| Q70 | - |  |  | SI | Puntaje de Score de riesgo de Morir por Bronconeum... |
| Q71 | - |  |  | SI | HLHT |
| Q72 | - |  |  | SI | Origen de Paciente |
| Q73 | - |  |  | SI | 1.- Fecha de Alta |
| Q74 | - |  |  | SI | 2.- Fecha de Alta |
| Q75 | - |  |  | SI | 3.- Fecha de Alta |
| Q76 | - |  |  | SI | 4.- Fecha de Alta |
| Q77 | - |  |  | SI | Clasificación de Control |
| Q78 | - |  |  | SI | Inhaladores de Rescate |
| Q79 | - |  |  | SI | Antecedentes de Descompensación |
| Q80 | - |  |  | SI | Antecedentes de Descompensación |
| Q81 | - |  |  | SI | Datos Relevantes Anamnesis/Examen Fisico |
| Q82 | - |  |  | SI | Vacuna Anti Influeza |
| Q83 | - |  |  | SI | Fecha ultimo Control |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*