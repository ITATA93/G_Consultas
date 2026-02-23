# SQLUser.OEC_ConsultCategICDDxOrd

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| ITM_ARCIM1_DR | varchar |  | FK | SI | Des Ref ARCIM1 |
| ITM_ARCIM2_DR | varchar |  | FK | SI | Des Ref ARCIM2 |
| ITM_ARCIM3_DR | varchar |  | FK | SI | Des Ref ARCIM3 |
| ITM_ARCIM4_DR | varchar |  | FK | SI | Des Ref ARCIM4 |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nosocomial infection type |
| Q01N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Urinary tract infection (UTI) |
| Q04 | - |  |  | SI | Diagnostic date |
| Q05 | - |  |  | SI | UTI cause |
| Q05ObsDR | - |  |  | SI | UTI cause DR |
| Q06 | - |  |  | SI | Urinary catheter type |
| Q06ObsDR | - |  |  | SI | Urinary catheter type DR |
| Q07 | - |  |  | SI | Catheterization date |
| Q08 | - |  |  | SI | UTI catheterization the last hour |
| Q08ObsDR | - |  |  | SI | UTI catheterization the last hour DR |
| Q09 | - |  |  | SI | UTI sign and symptoms |
| Q09N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Urinary exams / tests |
| Q11N | - |  |  | SI | Note |
| Q13 | - |  |  | SI | Laboratory diagnostic nosocomial infections |
| Q14 | - |  |  | SI | Note |
| Q15 | - |  |  | SI | Hospital-acquired pneumonia (HAP) |
| Q16 | - |  |  | SI | Diagnostic date |
| Q17 | - |  |  | SI | Respiratory infection type |
| Q17ObsDR | - |  |  | SI | Respiratory infection type DR |
| Q18 | - |  |  | SI | Respiratory infection cause |
| Q18N | - |  |  | SI | Note |
| Q18ObsDR | - |  |  | SI | Respiratory infection cause DR |
| Q20 | - |  |  | SI | Respiratory ventilation |
| Q20ObsDR | - |  |  | SI | Respiratory ventilation DR |
| Q21 | - |  |  | SI | Respiratory Ventilation the last hour |
| Q21ObsDR | - |  |  | SI | Respiratory Ventilation the last hour DR |
| Q22 | - |  |  | SI | Respiratory signs and symptoms |
| Q22N | - |  |  | SI | Note |
| Q24 | - |  |  | SI | Laboratory diagnostic HAP |
| Q25 | - |  |  | SI | Note |
| Q26 | - |  |  | SI | Catheter-associated Intravascular Infection |
| Q27 | - |  |  | SI | Diagnostic date |
| Q28 | - |  |  | SI | Date catheter from |
| Q29 | - |  |  | SI | Date catheter to |
| Q30 | - |  |  | SI | Intravascular catheter type |
| Q30ObsDR | - |  |  | SI | Intravascular catheter type DR |
| Q31 | - |  |  | SI | Intravascular catheter  localization |
| Q31ObsDR | - |  |  | SI | Intravascular catheter  localization DR |
| Q32 | - |  |  | SI | Intravascular infection signs and symptoms |
| Q32N | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Laboratory diagnostic intravascular infection |
| Q34 | - |  |  | SI | Note |
| Q35 | - |  |  | SI | Surgical site infection (SSI) |
| Q36 | - |  |  | SI | SSI diagnostic date |
| Q37 | - |  |  | SI | Date Surgery |
| Q38 | - |  |  | SI | Implantat in situ? |
| Q38N | - |  |  | SI | Note |
| Q38ObsDR | - |  |  | SI | Implantat in situ? DR |
| Q40 | - |  |  | SI | SSI Infection type |
| Q40ObsDR | - |  |  | SI | SSI Infection type DR |
| Q41 | - |  |  | SI | SSI Signs and Symptoms |
| Q41N | - |  |  | SI | Note |
| Q42 | - |  |  | SI | SSI  exams / tests |
| Q43 | - |  |  | SI | Laboratory diagnostic SSI |
| Q44 | - |  |  | SI | Note |
| Q45 | - |  |  | SI | Bacteremia |
| Q46 | - |  |  | SI | Diagnostic Date |
| Q47 | - |  |  | SI | Bacteremia cause |
| Q47N | - |  |  | SI | Note |
| Q47ObsDR | - |  |  | SI | Bacteremia cause DR |
| Q49 | - |  |  | SI | Bacteremia exams / test |
| Q50 | - |  |  | SI | Bacteremia signs and symptoms |
| Q50N | - |  |  | SI | Note |
| Q51 | - |  |  | SI | Laboratory diagnostic bacteremia |
| Q52 | - |  |  | SI | Note |
| Q53 | - |  |  | SI | Methicillin-resistant Staphylococcus aureus (MRSA) |
| Q54 | - |  |  | SI | Diagnostic date |
| Q55 | - |  |  | SI | MRSA admission screening |
| Q55ObsDR | - |  |  | SI | MRSA admission screening DR |
| Q56 | - |  |  | SI | MRSA Screening |
| Q56N | - |  |  | SI | Note |
| Q58 | - |  |  | SI | MRSA signs and symptoms |
| Q58N | - |  |  | SI | Note |
| Q60 | - |  |  | SI | Note |
| Q64 | - |  |  | SI | Date |
| Q65 | - |  |  | SI | Time |
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