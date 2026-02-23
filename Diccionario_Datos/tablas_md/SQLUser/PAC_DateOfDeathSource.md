# SQLUser.PAC_DateOfDeathSource

**Schema:** SQLUser
**Columnas:** 254
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DODSRC_RowId | bigint | PK |  | NO | - |
| DODSRC_Code | varchar |  |  | NO | Code |
| DODSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DODSRC_CreatedDate | date |  |  | SI | Created Date |
| DODSRC_CreatedTime | time |  |  | SI | Created Time |
| DODSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DODSRC_DateFrom | date |  |  | SI | DateFrom |
| DODSRC_DateTo | date |  |  | SI | DateTo |
| DODSRC_Desc | varchar |  |  | NO | Description |
| DODSRC_Owner | varchar |  |  | SI | Owner |
| DODSRC_UpdatedDate | date |  |  | SI | Updated Date |
| DODSRC_UpdatedTime | time |  |  | SI | Updated Time |
| DODSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Plate type |
| Q04 | - |  |  | SI | Estimated blood loss (EBL) (ml) |
| Q05 | - |  |  | SI | ml |
| Q06 | - |  |  | SI | Examination under anesthesia (EUA) |
| Q07 | - |  |  | SI | Tourniquet |
| Q08 | - |  |  | SI | PF inferior grade |
| Q09 | - |  |  | SI | PF Inferior size (mm) |
| Q10 | - |  |  | SI | PF (M) cartilage debrided |
| Q100 | - |  |  | SI | Lateral LM |
| Q101 | - |  |  | SI | Lateral LM findings |
| Q102 | - |  |  | SI | Lateral LM size |
| Q103 | - |  |  | SI | Lateral LM tear type |
| Q104 | - |  |  | SI | Lateral LM treatment |
| Q105 | - |  |  | SI | Anterior LM |
| Q106 | - |  |  | SI | Anterior LM findings |
| Q107 | - |  |  | SI | Anterior LM size |
| Q108 | - |  |  | SI | Anterior LM tear type |
| Q109 | - |  |  | SI | Anterior LM treatment |
| Q11 | - |  |  | SI | PF superior grade |
| Q110 | - |  |  | SI | Number of holes |
| Q111 | - |  |  | SI | Lateral cartilage treatment |
| Q112 | - |  |  | SI | ACL finding |
| Q113 | - |  |  | SI | Anterior Collateral Ligament posterolateral Bundle... |
| Q114 | - |  |  | SI | Anterior Collateral Ligament Anteromedial Bundle (... |
| Q115 | - |  |  | SI | PCL finding |
| Q116 | - |  |  | SI | Posterior Collateral Ligament posteromedial Bundle... |
| Q117 | - |  |  | SI | Details |
| Q118 | - |  |  | SI | Findings |
| Q119 | - |  |  | SI | Size (mm) |
| Q12 | - |  |  | SI | PF superior size (mm) |
| Q120 | - |  |  | SI | Tear type |
| Q121 | - |  |  | SI | Treatment |
| Q122 | - |  |  | SI | Posterior MM |
| Q123 | - |  |  | SI | Posterior MM findings |
| Q124 | - |  |  | SI | Posterior MM size |
| Q125 | - |  |  | SI | Posterior MM tear type |
| Q126 | - |  |  | SI | Posterior MM treatment |
| Q127 | - |  |  | SI | Medial MM |
| Q128 | - |  |  | SI | Medial MM findings |
| Q129 | - |  |  | SI | Medial MM size |
| Q13 | - |  |  | SI | PF (L) cartilage debrided |
| Q130 | - |  |  | SI | Posterior MM findings |
| Q131 | - |  |  | SI | Medial MM findings |
| Q132 | - |  |  | SI | Anterior MM findings |
| Q133 | - |  |  | SI | Posterior MM size |
| Q134 | - |  |  | SI | Medial MM size |
| Q135 | - |  |  | SI | Anterior MM size |
| Q136 | - |  |  | SI | Posterior MM tear type |
| Q137 | - |  |  | SI | Medial MM tear type |
| Q138 | - |  |  | SI | Anterior MM tear type |
| Q139 | - |  |  | SI | Posterior MM treatment |
| Q14 | - |  |  | SI | Sulcus grade |
| Q140 | - |  |  | SI | Medial MM treatment |
| Q141 | - |  |  | SI | Anterior MM treatment |
| Q142 | - |  |  | SI | Posterior LM findings |
| Q143 | - |  |  | SI | Lateral LM findings |
| Q144 | - |  |  | SI | Anterior LM findings |
| Q145 | - |  |  | SI | Posterior LM size |
| Q146 | - |  |  | SI | Lateral LM size |
| Q147 | - |  |  | SI | Anterior LM size |
| Q148 | - |  |  | SI | Posterior LM tear type |
| Q149 | - |  |  | SI | Lateral LM tear type |
| Q15 | - |  |  | SI | Sulcus size (mm) |
| Q150 | - |  |  | SI | Anterior LM tear type |
| Q151 | - |  |  | SI | Posterior LM treatment |
| Q152 | - |  |  | SI | Lateral LM treatment |
| Q153 | - |  |  | SI | Anterior LM treatment |
| Q154 | - |  |  | SI | Findings |
| Q155 | - |  |  | SI | Findings |
| Q156 | - |  |  | SI | Findings |
| Q157 | - |  |  | SI | Size (mm) |
| Q158 | - |  |  | SI | Size (mm) |
| Q159 | - |  |  | SI | Size (mm) |
| Q16 | - |  |  | SI | Sulcus treatment |
| Q160 | - |  |  | SI | Tear type |
| Q161 | - |  |  | SI | Tear type |
| Q162 | - |  |  | SI | Tear type |
| Q163 | - |  |  | SI | Treatment |
| Q164 | - |  |  | SI | Treatment |
| Q165 | - |  |  | SI | Treatment |
| Q166 | - |  |  | SI | Findings |
| Q167 | - |  |  | SI | Findings |
| Q168 | - |  |  | SI | Findings |
| Q169 | - |  |  | SI | Size (mm) |
| Q17 | - |  |  | SI | Medial cartilage grade |
| Q170 | - |  |  | SI | Size (mm) |
| Q171 | - |  |  | SI | Size (mm) |
| Q172 | - |  |  | SI | Tear type |
| Q173 | - |  |  | SI | Tear type |
| Q174 | - |  |  | SI | Tear type |
| Q175 | - |  |  | SI | Treatment |
| Q176 | - |  |  | SI | Treatment |
| Q177 | - |  |  | SI | Treatment |
| Q178 | - |  |  | SI | Findings |
| Q179 | - |  |  | SI | Findings |
| Q18 | - |  |  | SI | Medial cartilage size (mm) |
| Q180 | - |  |  | SI | Findings |
| Q181 | - |  |  | SI | Size (mm) |
| Q182 | - |  |  | SI | Size (mm) |
| Q183 | - |  |  | SI | Size (mm) |
| Q184 | - |  |  | SI | Tear type |
| Q185 | - |  |  | SI | Tear type |
| Q186 | - |  |  | SI | Tear type |
| Q187 | - |  |  | SI | Treatment |
| Q188 | - |  |  | SI | Treatment |
| Q189 | - |  |  | SI | Treatment |
| Q19 | - |  |  | SI | Medial cartilage treatment |
| Q190 | - |  |  | SI | Findings |
| Q191 | - |  |  | SI | Findings |
| Q192 | - |  |  | SI | Findings |
| Q193 | - |  |  | SI | Size (mm) |
| Q194 | - |  |  | SI | Size (mm) |
| Q195 | - |  |  | SI | Size (mm) |
| Q196 | - |  |  | SI | Tear type |
| Q197 | - |  |  | SI | Tear type |
| Q198 | - |  |  | SI | Tear type |
| Q199 | - |  |  | SI | Treatment |
| Q20 | - |  |  | SI | Lateral cartilage grade |
| Q200 | - |  |  | SI | Treatment |
| Q201 | - |  |  | SI | Treatment |
| Q21 | - |  |  | SI | Lateral cartilage size (mm) |
| Q22 | - |  |  | SI | Lateral cartilage treatment |
| Q23 | - |  |  | SI | ACL finding |
| Q24 | - |  |  | SI | Anterior Collateral Ligament posterolateral Bundle... |
| Q25 | - |  |  | SI | Anterior Collateral Ligament Anteromedial Bundle (... |
| Q26 | - |  |  | SI | PCL finding |
| Q27 | - |  |  | SI | Posterior Collateral Ligament Posteromedial Bundle... |
| Q28 | - |  |  | SI | Details |
| Q29 | - |  |  | SI | Findings |
| Q30 | - |  |  | SI | Size (mm) |
| Q31 | - |  |  | SI | Tear type |
| Q32 | - |  |  | SI | Treatment |
| Q33 | - |  |  | SI | Posterior MM |
| Q34 | - |  |  | SI | Posterior MM findings |
| Q35 | - |  |  | SI | Posterior MM size (mm) |
| Q36 | - |  |  | SI | Posterior MM tear type |
| Q37 | - |  |  | SI | Posterior MM treatment |
| Q38 | - |  |  | SI | Medial MM |
| Q39 | - |  |  | SI | Medial MM findings |
| Q40 | - |  |  | SI | Medial MM findings |
| Q41 | - |  |  | SI | Medial MM size (mm) |
| Q42 | - |  |  | SI | Medial MM tear type |
| Q43 | - |  |  | SI | Medial MM treatment |
| Q44 | - |  |  | SI | Anterior MM |
| Q45 | - |  |  | SI | Anterior MM findings |
| Q46 | - |  |  | SI | Anterior MM size (mm) |
| Q47 | - |  |  | SI | Anterior MM tear type |
| Q48 | - |  |  | SI | Anterior MM treatment |
| Q49 | - |  |  | SI | Details |
| Q50 | - |  |  | SI | Findings |
| Q51 | - |  |  | SI | Size (mm) |
| Q52 | - |  |  | SI | Tear type |
| Q53 | - |  |  | SI | Treatment |
| Q54 | - |  |  | SI | Posterior LM |
| Q55 | - |  |  | SI | Posterior LM findings |
| Q56 | - |  |  | SI | Posterior LM size (mm) |
| Q57 | - |  |  | SI | Posterior LM tear type |
| Q58 | - |  |  | SI | Posterior LM treatment |
| Q59 | - |  |  | SI | Lateral LM |
| Q60 | - |  |  | SI | Lateral LM findings |
| Q61 | - |  |  | SI | Lateral LM size (mm) |
| Q62 | - |  |  | SI | Lateral LM tear type |
| Q63 | - |  |  | SI | Lateral LM treatment |
| Q64 | - |  |  | SI | Anterior LM |
| Q65 | - |  |  | SI | Anterior LM findings |
| Q66 | - |  |  | SI | Anterior LM size (mm) |
| Q67 | - |  |  | SI | Anterior LM tear type |
| Q68 | - |  |  | SI | Anterior LM treatment |
| Q69 | - |  |  | SI | PF inferior grade |
| Q70 | - |  |  | SI | PF Inferior size |
| Q71 | - |  |  | SI | PF (M) cartilage debrided |
| Q72 | - |  |  | SI | PF superior grade |
| Q73 | - |  |  | SI | PF superior size |
| Q74 | - |  |  | SI | PF (L) cartilage debrided |
| Q75 | - |  |  | SI | Sulcus grade |
| Q76 | - |  |  | SI | Salcus size (mm) |
| Q77 | - |  |  | SI | Salcus Treatment |
| Q78 | - |  |  | SI | Medial cartilage grade |
| Q79 | - |  |  | SI | Medial cartilage size (mm) |
| Q80 | - |  |  | SI | Medial cartilage treatment |
| Q81 | - |  |  | SI | Lateral cartilage grade |
| Q82 | - |  |  | SI | Lateral cartilage size (mm) |
| Q83 | - |  |  | SI | Medial MM tear type |
| Q84 | - |  |  | SI | Medial MM treatment |
| Q85 | - |  |  | SI | Anterior MM |
| Q86 | - |  |  | SI | Anterior MM findings |
| Q87 | - |  |  | SI | Anterior MM size |
| Q88 | - |  |  | SI | Anterior MM tear type |
| Q89 | - |  |  | SI | Anterior MM treatment |
| Q90 | - |  |  | SI | Details |
| Q91 | - |  |  | SI | Findings |
| Q92 | - |  |  | SI | Size |
| Q93 | - |  |  | SI | Tear type |
| Q94 | - |  |  | SI | Treatment |
| Q95 | - |  |  | SI | Posterior LM |
| Q96 | - |  |  | SI | Posterior LM findings |
| Q97 | - |  |  | SI | Posterior LM size |
| Q98 | - |  |  | SI | Posterior LM tear type |
| Q99 | - |  |  | SI | Posterior LM treatment |
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