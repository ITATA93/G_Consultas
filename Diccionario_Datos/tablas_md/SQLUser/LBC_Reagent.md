# SQLUser.LBC_Reagent

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRE_RowID | bigint | PK |  | NO | - |
| LBCRE_Code | varchar |  |  | NO | Code |
| LBCRE_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCRE_CreatedDate | date |  |  | SI | Created Date |
| LBCRE_CreatedTime | time |  |  | SI | Created Time |
| LBCRE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRE_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRE_DateTo | date |  |  | SI | Last day the record is active |
| LBCRE_Desc | varchar |  |  | NO | Description |
| LBCRE_Owner | varchar |  |  | SI | Owner |
| LBCRE_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRE_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antecedentes de Enfermedades Concomitantes |
| Q02 | - |  |  | SI | Derivación desde APS para Diagnóstico en Nivel Sec... |
| Q03 | - |  |  | SI | Control con Neurólogo |
| Q04 | - |  |  | SI | Última Crisis de Epilepsia |
| Q05 | - |  |  | SI | Fecha Última Crisis |
| Q06 | - |  |  | SI | N° de Episodios |
| Q07 | - |  |  | SI | GOT |
| Q07ObsDR | - |  |  | SI | GOT DR |
| Q08 | - |  |  | SI | GPT |
| Q08ObsDR | - |  |  | SI | GPT DR |
| Q09 | - |  |  | SI | Creatinina |
| Q09ObsDR | - |  |  | SI | Creatinina DR |
| Q10 | - |  |  | SI | Hemograma |
| Q10ObsDR | - |  |  | SI | Hemograma DR |
| Q11 | - |  |  | SI | Sodio |
| Q11ObsDR | - |  |  | SI | Sodio DR |
| Q12 | - |  |  | SI | Potasio |
| Q12ObsDR | - |  |  | SI | Potasio DR |
| Q13 | - |  |  | SI | Cloro |
| Q13ObsDR | - |  |  | SI | Cloro DR |
| Q14 | - |  |  | SI | INR |
| Q14ObsDR | - |  |  | SI | INR DR |
| Q15 | - |  |  | SI | Otro Examen |
| Q16 | - |  |  | SI | Tratamiento Farmacológico |
| Q17 | - |  |  | SI | Fármacos |
| Q18 | - |  |  | SI | Efectos Secundarios al Tratamiento |
| Q19 | - |  |  | SI | Descriva Efectos Secundarios |
| Q20 | - |  |  | SI | Adherencia |
| Q21 | - |  |  | SI | Tratamiento Anticonceptivo |
| Q22 | - |  |  | SI | Describa Tratamiento Anticonceptivo |
| Q23 | - |  |  | SI | Tratamiento Adicional |
| Q24 | - |  |  | SI | Describa Tratamiento |
| Q25 | - |  |  | SI | Derivación Neurólogo |
| Q26 | - |  |  | SI | Control de Embarazo |
| Q27 | - |  |  | SI | Tratamiento Ácido Fólico |
| Q28 | - |  |  | SI | Laborales |
| Q29 | - |  |  | SI | Económicos |
| Q30 | - |  |  | SI | Psicológicos |
| Q31 | - |  |  | SI | Familiares |
| Q32 | - |  |  | SI | Consumo de Tabaco |
| Q33 | - |  |  | SI | Consumo de Alcohol |
| Q34 | - |  |  | SI | Consumo de Drogas |
| Q35 | - |  |  | SI | Trastorno de Sueño |
| Q36 | - |  |  | SI | Otro Fármaco |
| Q37 | - |  |  | SI | Frecuencia de Consumo |
| Q38 | - |  |  | SI | Tipo de Droga |
| Q39 | - |  |  | SI | TP |
| Q39ObsDR | - |  |  | SI | TP DR |
| Q40 | - |  |  | SI | Electrolitos Plasmáticos |
| Q41 | - |  |  | SI | Fecha Último Control Neurólogo |
| Q42 | - |  |  | SI | Fecha de Diagnóstico de Epilepsia |
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