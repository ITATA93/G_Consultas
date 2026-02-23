# SQLUser.MR_AdmMedicationHistory

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEDHIST_RowId | varchar | PK |  | NO | - |
| MEDHISTMRADMID | varchar |  |  | NO | This Property is not stored.  Only needed for RowI... |
| MEDHIST_Comments | varchar |  |  | SI | Comments |
| MEDHIST_CreatedDate | date |  |  | SI | Created Date |
| MEDHIST_CreatedHospital_DR | bigint |  | FK | SI | Des Ref Created Hospital |
| MEDHIST_CreatedTime | time |  |  | SI | Created Time |
| MEDHIST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDHIST_MRAdm_DR | bigint |  | FK | SI | Des Ref MRADM |
| MEDHIST_NoMedHistory | varchar |  |  | SI | Patient Reports No Medication History |
| MEDHIST_PrimarySource_DR | bigint |  | FK | SI | Des Ref PHCMedHistInformSource |
| MEDHIST_ReasonForCorrection_DR | bigint |  | FK | SI | Reason for Correction |
| MEDHIST_SecondarySources | varchar |  |  | SI | Secondary Sources |
| MEDHIST_Status | varchar |  |  | SI | Status |
| MEDHIST_UpdateDate | date |  |  | SI | UpdateDate |
| MEDHIST_UpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MEDHIST_UpdateTime | time |  |  | SI | UpdateTime |
| MEDHIST_UpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| Q01 | - |  |  | SI | RUN |
| Q02 | - |  |  | SI | Nombres |
| Q03 | - |  |  | SI | Apellido Paterno |
| Q04 | - |  |  | SI | Apellido Materno |
| Q05 | - |  |  | SI | Sexo |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Dirección |
| Q09 | - |  |  | SI | Región |
| Q10 | - |  |  | SI | Ciudad/Localidad |
| Q11 | - |  |  | SI | Comuna |
| Q12 | - |  |  | SI | Teléfono |
| Q13 | - |  |  | SI | Previsión |
| Q14 | - |  |  | SI | Profesional Responsable |
| Q15 | - |  |  | SI | Región |
| Q16 | - |  |  | SI | Provincia |
| Q17 | - |  |  | SI | Comuna |
| Q18 | - |  |  | SI | Dirección |
| Q19 | - |  |  | SI | Laboratorio/Hospital |
| Q20 | - |  |  | SI | Unidad |
| Q21 | - |  |  | SI | Correo Electronico |
| Q22 | - |  |  | SI | Fono |
| Q23 | - |  |  | SI | Fax |
| Q24 | - |  |  | SI | Tipo de Muestra |
| Q25 | - |  |  | SI | Fecha Obtención Suero |
| Q26 | - |  |  | SI | Muestra |
| Q27 | - |  |  | SI | Fecha obtención Respiratoria/Orina |
| Q28 | - |  |  | SI | Fecha envío ISP |
| Q29 | - |  |  | SI | Fecha Inicio Exantema |
| Q30 | - |  |  | SI | Fecha Ultima Vacuna Rubéola |
| Q31 | - |  |  | SI | Fecha Última Vacuna Sarampión |
| Q32 | - |  |  | SI | Fiebre Sobre 38°c |
| Q33 | - |  |  | SI | Conjuntivitis |
| Q34 | - |  |  | SI | Linfoadenopatias |
| Q35 | - |  |  | SI | Artralgias |
| Q36 | - |  |  | SI | Tos |
| Q37 | - |  |  | SI | Coriza |
| Q38 | - |  |  | SI | Fecha Inicio Fiebre |
| Q39 | - |  |  | SI | Plan |
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