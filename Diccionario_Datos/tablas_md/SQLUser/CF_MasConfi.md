# SQLUser.CF_MasConfi

**Schema:** SQLUser
**Columnas:** 145
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MACF_RowID | bigint | PK |  | NO | - |
| ChildQ88DR | - |  |  | SI | Child Reference: Amputación de extremidad Especifi... |
| MACF_Active | varchar |  |  | SI | Active |
| MACF_CT_DR | double |  | FK | SI | Des Ref to CFCT |
| MACF_Description | varchar |  |  | SI | Desc |
| MACF_IN_DR | double |  | FK | SI | Inventory |
| MACF_LogonAttempts | double |  |  | SI | User Logon Attempts |
| MACF_OE_DR | bigint |  | FK | SI | Des Ref To OECF |
| MACF_PH_DR | bigint |  | FK | SI | Des Ref To PHCF |
| MACF_PatCnfDR | bigint |  | FK | SI | Patient Config |
| MACF_RB_DR | bigint |  | FK | SI | Resource Booking |
| MACF_RT_DR | bigint |  | FK | SI | Record Tracking |
| Q01 | - |  |  | SI | ANTECEDENTES CLÍNICOS |
| Q02 | - |  |  | SI | Resultado EFAM A |
| Q03 | - |  |  | SI | Resultado EFAM B |
| Q04 | - |  |  | SI | Resultado de MMSE |
| Q05 | - |  |  | SI | Mamografía |
| Q06 | - |  |  | SI | Papanicolau |
| Q07 | - |  |  | SI | Vacunación Influenza |
| Q08 | - |  |  | SI | Vacunación Neumococo |
| Q09 | - |  |  | SI | Fecha Registros Antecedentes RUI |
| Q09ObsDR | - |  |  | SI | Fecha Registros Antecedentes RUI DR |
| Q10 | - |  |  | SI | Fecha Último Registro RUI |
| Q11 | - |  |  | SI | Beneficiario Programa Alimentario |
| Q12 | - |  |  | SI | Fecha Resultado EFAM A |
| Q13 | - |  |  | SI | Fecha Resultado EFAM B |
| Q14 | - |  |  | SI | Fecha Resultado de MMSE |
| Q15 | - |  |  | SI | Fecha Mamografía |
| Q16 | - |  |  | SI | Fecha Papanicolau |
| Q17 | - |  |  | SI | Fecha Vacunación Influenza |
| Q18 | - |  |  | SI | Fecha Vacunación Neumococo |
| Q19 | - |  |  | SI | Fecha Beneficiario Programa Alimentario |
| Q20 | - |  |  | SI | CHEQUEO DIAGNÓSTICOS CRÓNICOS |
| Q21 | - |  |  | SI | Enfermedad Renal Crónica |
| Q21ObsDR | - |  |  | SI | Enfermedad Renal Crónica DR |
| Q22 | - |  |  | SI | Fecha Enfermedad Renal Crónica |
| Q23 | - |  |  | SI | EPOC |
| Q24 | - |  |  | SI | Fecha EPOC |
| Q25 | - |  |  | SI | Nivel Severidad EPOC |
| Q26 | - |  |  | SI | Diabetes Mellitus |
| Q27 | - |  |  | SI | Fecha Diabetes Mellitus |
| Q28 | - |  |  | SI | Resultado Riesgo Ulceración |
| Q28ObsDR | - |  |  | SI | Resultado Riesgo Ulceración DR |
| Q29 | - |  |  | SI | Fecha Resultado Riesgo Ulceración |
| Q30 | - |  |  | SI | Amputación de extremidad |
| Q31 | - |  |  | SI | Fecha Amputación de extremidad |
| Q32 | - |  |  | SI | ACV |
| Q33 | - |  |  | SI | Fecha ACV |
| Q34 | - |  |  | SI | IAM |
| Q35 | - |  |  | SI | Fecha IAM |
| Q36 | - |  |  | SI | Sordera |
| Q37 | - |  |  | SI | Fecha Sordera |
| Q38 | - |  |  | SI | Retraso Mental |
| Q39 | - |  |  | SI | Fecha Retraso Mental |
| Q40 | - |  |  | SI | Fragilidad |
| Q41 | - |  |  | SI | Fecha Fragilidad |
| Q42 | - |  |  | SI | MORBILIDAD |
| Q43 | - |  |  | SI | Asistencia a Urgencias por Patología Crónica |
| Q44 | - |  |  | SI | Fecha Asistencia a Urgencias por Patología Crónica |
| Q45 | - |  |  | SI | Hospitalización por Patología Crónica |
| Q46 | - |  |  | SI | Fecha Hospitalización por patología crónica |
| Q47 | - |  |  | SI | HÁBITOS |
| Q48 | - |  |  | SI | Hábitos Alimenticios |
| Q49 | - |  |  | SI | Fecha Hábitos Alimenticios |
| Q50 | - |  |  | SI | Actividad Física Actual |
| Q51 | - |  |  | SI | Fecha Actividad Física Actual |
| Q52 | - |  |  | SI | Tabaquismo |
| Q53 | - |  |  | SI | Fecha Tabaquismo |
| Q54 | - |  |  | SI | Alcohol |
| Q55 | - |  |  | SI | Fecha Consumo de alcohol |
| Q56 | - |  |  | SI | Consumo de Drogas |
| Q57 | - |  |  | SI | Fecha Consumo de drogas |
| Q58 | - |  |  | SI | Alergia a Medicamentos |
| Q59 | - |  |  | SI | Fecha Alergia a Medicamentos |
| Q60 | - |  |  | SI | Monitoreo a Distancia |
| Q61 | - |  |  | SI | Fecha Monitoreo a Distancia |
| Q62 | - |  |  | SI | ANTECEDENTES FAMILIARES |
| Q63 | - |  |  | SI | Familiar con Condición Crónica |
| Q64 | - |  |  | SI | Fecha Familiar con Condición Crónica |
| Q65 | - |  |  | SI | Número de Integrantes Núcleo Familiar |
| Q65ObsDR | - |  |  | SI | Número de Integrantes Núcleo Familiar DR |
| Q66 | - |  |  | SI | Fecha Número de Integrantes Nucleo Familiar |
| Q67 | - |  |  | SI | Red de apoyo |
| Q68 | - |  |  | SI | Fecha Red de Apoyo |
| Q69 | - |  |  | SI | Red de apoyo Principal |
| Q70 | - |  |  | SI | Fecha Red de Apoyo Principal |
| Q71 | - |  |  | SI | Institucionalizado |
| Q72 | - |  |  | SI | Fecha Institucionalizado |
| Q73 | - |  |  | SI | Situación de Calle |
| Q74 | - |  |  | SI | Fecha Situación de Calle |
| Q75 | - |  |  | SI | ANTECEDENTES DE SALUD MENTAL |
| Q76 | - |  |  | SI | Ideación / Intento Suicida |
| Q77 | - |  |  | SI | Fecha Ideación / Intento Suicida |
| Q78 | - |  |  | SI | Síntomas Psicóticos |
| Q79 | - |  |  | SI | Fecha Síntomas Psicóticos |
| Q80 | - |  |  | SI | Factores de Riesgo - Víctima de Violencia |
| Q81 | - |  |  | SI | Fecha Factores de Riesgo - Víctima de Violencia |
| Q82 | - |  |  | SI | Factores de Riesgo - Víctima de Abuso Sexual |
| Q83 | - |  |  | SI | Fecha Factores de Riesgo - Víctima de Abuso Sexual |
| Q84 | - |  |  | SI | Amputación de extremidad por DM |
| Q85 | - |  |  | SI | Fecha Amputación de extremidad Por DM |
| Q86 | - |  |  | SI | Hora Registros Antecedentes RUI |
| Q86ObsDR | - |  |  | SI | Hora Registros Antecedentes RUI DR |
| Q87 | - |  |  | SI | Hora Último Registro RUI |
| Q89 | - |  |  | SI | Etapa Renal Crónica |
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