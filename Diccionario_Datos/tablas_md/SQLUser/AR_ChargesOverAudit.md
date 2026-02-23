# SQLUser.AR_ChargesOverAudit

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COV_RowId | bigint | PK |  | NO | - |
| COV_Amount | double |  |  | SI | Amount |
| COV_ApplyGST | varchar |  |  | SI | Apply GST |
| COV_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| COV_BillQty | double |  |  | SI | Bill Qty |
| COV_DateFrom | date |  |  | SI | DateFrom |
| COV_DateTo | date |  |  | SI | DateTo |
| COV_InsAssoc_DR | bigint |  | FK | SI | Des Ref InsAssoc |
| COV_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| COV_InsuranceExclude | bigint |  |  | SI | Des Ref Insurance Type |
| COV_ItemGroup | varchar |  |  | SI | ItemGroup |
| COV_Key | varchar |  |  | SI | Key |
| COV_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| COV_PatientAmt | double |  |  | SI | PatientAmt |
| COV_PatientPercentage | double |  |  | SI | PatientPercentage |
| COV_Percentage | varchar |  |  | SI | Percentage |
| COV_Price | double |  |  | SI | Price |
| COV_ReasonNotShow_DR | bigint |  | FK | SI | Des Ref  ReasonNotShow |
| COV_ServTax_DR | bigint |  | FK | SI | Des Ref ServTax |
| COV_UpdateDate | date |  |  | SI | UpdateDate |
| COV_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| COV_UpdateTime | time |  |  | SI | UpdateTime |
| COV_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ChildQ32DR | - |  |  | SI | Child Reference: Identificación con quienes cohabi... |
| Q01 | - |  |  | SI | Fecha  de Registro del Informe |
| Q02 | - |  |  | SI | Hora de Registro del Informe |
| Q03 | - |  |  | SI | Responsable del Registro del Informe |
| Q04 | - |  |  | SI | I. Datos de Identificación del paciente |
| Q05 | - |  |  | SI | Teléfono Celular |
| Q06 | - |  |  | SI | Correo Electrónico |
| Q07 | - |  |  | SI | Domicilio Villa / Población |
| Q08 | - |  |  | SI | Número |
| Q09 | - |  |  | SI | Comuna |
| Q10 | - |  |  | SI | Estado civil |
| Q11 | - |  |  | SI | Sistema de Salud |
| Q12 | - |  |  | SI | Motivo de solicitud de certificación |
| Q13 | - |  |  | SI | II. Datos de Identificación del representante |
| Q14 | - |  |  | SI | Representante |
| Q15 | - |  |  | SI | Nombres y Apellidos |
| Q16 | - |  |  | SI | R.U.N.  (99.999.999-9) |
| Q17 | - |  |  | SI | Correo Electrónico |
| Q18 | - |  |  | SI | Teléfono |
| Q19 | - |  |  | SI | Relación con el interesado |
| Q20 | - |  |  | SI | III. Situación escolar y laboral del Paciente |
| Q21 | - |  |  | SI | Nivel de escolaridad alcanzado |
| Q22 | - |  |  | SI | Actividad o actividades que desempeña actualmente |
| Q23 | - |  |  | SI | Estudia |
| Q24 | - |  |  | SI | Trabaja |
| Q25 | - |  |  | SI | Rubro en que se desempeña |
| Q26 | - |  |  | SI | Dificultades que presenta en el trabajo |
| Q27 | - |  |  | SI | Situación ocupacional |
| Q28 | - |  |  | SI | Tipo de pensión |
| Q29 | - |  |  | SI | Tipo de jubilación |
| Q30 | - |  |  | SI | PIE: Programa de Integración Escolar |
| Q31 | - |  |  | SI | IV. Identificación con quienes cohabita paciente |
| Q33 | - |  |  | SI | Describa situación familiar actual |
| Q34 | - |  |  | SI | Paciente ¿tiene cuidador? |
| Q35 | - |  |  | SI | V. Descripción del cuidador(a) |
| Q36 | - |  |  | SI | Descripción cuidador/a principal |
| Q38 | - |  |  | SI | VI. Identificación de redes de apoyo y nivel de pa... |
| Q39 | - |  |  | SI | Red de apoyo principal con la que cuenta el pacien... |
| Q40 | - |  |  | SI | Primarias |
| Q41 | - |  |  | SI | Relación con interesado (Primarias) |
| Q42 | - |  |  | SI | Tipo de apoyo (Primarias) |
| Q43 | - |  |  | SI | Secundarias (clubes, agrupaciones, iglesia) |
| Q44 | - |  |  | SI | Relación con interesado (Secundarias) |
| Q45 | - |  |  | SI | Tipo de apoyo (Secundarias) |
| Q46 | - |  |  | SI | Institucionales (municipalidad, servicio salud, in... |
| Q47 | - |  |  | SI | Relación con interesado (Institucionales) |
| Q48 | - |  |  | SI | Tipo de apoyo (Institucionales) |
| Q49 | - |  |  | SI | Valoración general de la red de apoyo |
| Q50 | - |  |  | SI | Participación en actividades sociales (culturales,... |
| Q51 | - |  |  | SI | Participación en actividades sociales (Texto) |
| Q52 | - |  |  | SI | VII. Información sobre vivienda y entorno |
| Q53 | - |  |  | SI | Tipo de domicilio del paciente |
| Q54 | - |  |  | SI | Tipo de domicilio (Texto) |
| Q55 | - |  |  | SI | Sector |
| Q56 | - |  |  | SI | Identificación de barreras ambientales |
| Q57 | - |  |  | SI | Barreras al interior de la vivienda |
| Q58 | - |  |  | SI | Barreras del entorno de la vivienda |
| Q59 | - |  |  | SI | Habitación independiente |
| Q60 | - |  |  | SI | Baño dentro de la vivienda |
| Q61 | - |  |  | SI | Baño adaptado |
| Q62 | - |  |  | SI | Estado general de vivienda |
| Q63 | - |  |  | SI | Paciente tiene acceso a transporte |
| Q64 | - |  |  | SI | Tipo de transporte Publico |
| Q65 | - |  |  | SI | ¿El interesado tiene algún grado de limitación en ... |
| Q66 | - |  |  | SI | Comentarios |
| Q67 | - |  |  | SI | VIII. Datos de identificación de Asistente o Traba... |
| Q68 | - |  |  | SI | Nombre completo |
| Q69 | - |  |  | SI | R.U.N. (99.999.999-9) |
| Q70 | - |  |  | SI | Institución |
| Q71 | - |  |  | SI | Correo electrónico |
| Q72 | - |  |  | SI | Teléfono |
| Q73 | - |  |  | SI | Fecha Informe |
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