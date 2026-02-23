# SQLUser.PA_Mother

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOTH_RowId | bigint | PK |  | NO | - |
| MOTH_ArtifAbort | double |  |  | SI | Number of Artificial Abortions |
| MOTH_BreastFeed | varchar |  |  | SI | BreastFeed |
| MOTH_CertOfGestationLMP | varchar |  |  | SI | Certainty Of Gestation based on LMP |
| MOTH_ConsDegree_DR | bigint |  | FK | SI | Des Ref PregnConsDegree |
| MOTH_DateLMP | date |  |  | SI | Date of last Menstr Period |
| MOTH_ExpConfinDate | date |  |  | SI | Expected Date of Confinement(EDC) |
| MOTH_ExpDelivDate | date |  |  | SI | Expected Delivery Date |
| MOTH_FatherBldType_DR | bigint |  | FK | SI | Des Ref Blood Type |
| MOTH_FemaleBabies | double |  |  | SI | Number of Female Babies |
| MOTH_FinalWeight | varchar |  |  | SI | Final Weight |
| MOTH_FullTermDel | double |  |  | SI | Number of Full Term Delivery |
| MOTH_InitialWeight | varchar |  |  | SI | Initial Weight |
| MOTH_LastConsDate | date |  |  | SI | Last Consultation Date |
| MOTH_LastDelivDate | date |  |  | SI | Last Delivery Date |
| MOTH_LastDelivType | bigint |  |  | SI | Last Delivery METHOD(Des Ref ) |
| MOTH_MaleBabies | double |  |  | SI | Number of Male Babies |
| MOTH_MotherBldType_DR | bigint |  | FK | SI | Des Ref Blood Type |
| MOTH_NoOfPrevAdmissions | double |  |  | SI | No Of Prev Admissions |
| MOTH_PreTermDeliv | double |  |  | SI | Number of Pre Term Delivery |
| MOTH_PregnancyType_DR | bigint |  | FK | SI | Des Ref PregnancyType |
| MOTH_PrevCaesareanSections | double |  |  | SI | Prev Caesarean Sections |
| MOTH_PrevNeonatalDeaths | double |  |  | SI | Prev Neonatal Deaths |
| MOTH_PrevStillBirths | double |  |  | SI | Prev Still Births |
| MOTH_Remarks | varchar |  |  | SI | Remarks |
| MOTH_SpontAbort | double |  |  | SI | Number of Spontaneous Abortions |
| MOTH_SterilAfterDelivery | varchar |  |  | SI | Steril After Delivery |
| Q01 | - |  |  | SI | Nombre Paciente |
| Q02 | - |  |  | SI | Fecha Nacimiento |
| Q03 | - |  |  | SI | RUN |
| Q04 | - |  |  | SI | Fecha Admisión |
| Q05 | - |  |  | SI | Previsión |
| Q06 | - |  |  | SI | Ubicación |
| Q07 | - |  |  | SI | Hora Admisión |
| Q08 | - |  |  | SI | Cat Fecha Hora |
| Q09 | - |  |  | SI | Cat |
| Q10 | - |  |  | SI | Cat Realizado Por |
| Q11 | - |  |  | SI | Tiempo Espera |
| Q12 | - |  |  | SI | Inicio Atención Clínica |
| Q13 | - |  |  | SI | Motivo Consulta |
| Q14 | - |  |  | SI | Dig Principal Code |
| Q15 | - |  |  | SI | Diag Principal Desc |
| Q16 | - |  |  | SI | Diag Principal Com |
| Q17 | - |  |  | SI | NC Profesional |
| Q18 | - |  |  | SI | NC Fecha Hora |
| Q19 | - |  |  | SI | NC |
| Q20 | - |  |  | SI | SH Fecha Hora |
| Q21 | - |  |  | SI | SH Espcialidad |
| Q22 | - |  |  | SI | SH Servicio |
| Q23 | - |  |  | SI | NM Fecha Hora |
| Q24 | - |  |  | SI | NM User |
| Q25 | - |  |  | SI | NM |
| Q26 | - |  |  | SI | Alias |
| Q27 | - |  |  | SI | Nro Pasaporte |
| Q28 | - |  |  | SI | Nro Registro |
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