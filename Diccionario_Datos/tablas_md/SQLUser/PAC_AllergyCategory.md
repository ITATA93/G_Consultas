# SQLUser.PAC_AllergyCategory

**Schema:** SQLUser
**Columnas:** 207
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALRGCAT_RowId | bigint | PK |  | NO | - |
| ALRGCAT_AllergySeverity_DR | bigint |  | FK | SI | Allergy Severity |
| ALRGCAT_Code | varchar |  |  | NO | Code |
| ALRGCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALRGCAT_CreatedDate | date |  |  | SI | Created Date |
| ALRGCAT_CreatedTime | time |  |  | SI | Created Time |
| ALRGCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALRGCAT_CrossSensitivity | varchar |  |  | SI | Cross Sensitivity |
| ALRGCAT_DateFrom | date |  |  | SI | DateFrom |
| ALRGCAT_DateTo | date |  |  | SI | DateTo |
| ALRGCAT_Desc | varchar |  |  | NO | Description |
| ALRGCAT_HardStopText | varchar |  |  | SI | Hard Stop Guidance Text |
| ALRGCAT_IconName | varchar |  |  | SI | Icon Name |
| ALRGCAT_IconPriority | double |  |  | SI | Icon Priority |
| ALRGCAT_IsSensitivity | varchar |  |  | SI | Sensitivity Flag |
| ALRGCAT_Owner | varchar |  |  | SI | Owner |
| ALRGCAT_PharmAllergyGrp | varchar |  |  | SI | Pharmacy Allergy Group |
| ALRGCAT_UpdatedDate | date |  |  | SI | Updated Date |
| ALRGCAT_UpdatedTime | time |  |  | SI | Updated Time |
| ALRGCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fasting insulin |
| Q02 | - |  |  | SI | mcU/mL |
| Q03 | - |  |  | SI | Fasting glucose |
| Q04 | - |  |  | SI | mmol/L |
| Q05 | - |  |  | SI | HOMA-IR |
| Q06 | - |  |  | SI | The cut-off value for determining the presence of ... |
| Q07 | - |  |  | SI | Population |
| Q08 | - |  |  | SI | n |
| Q09 | - |  |  | SI | Age range(y) |
| Q10 | - |  |  | SI | Upper Limit for Men |
| Q100 | - |  |  | SI | n |
| Q101 | - |  |  | SI | n |
| Q102 | - |  |  | SI | n |
| Q103 | - |  |  | SI | n |
| Q104 | - |  |  | SI | n |
| Q105 | - |  |  | SI | Age range(y) |
| Q106 | - |  |  | SI | Age range(y) |
| Q107 | - |  |  | SI | Age range(y) |
| Q108 | - |  |  | SI | Age range(y) |
| Q109 | - |  |  | SI | Age range(y) |
| Q11 | - |  |  | SI | Upper Limit for Women |
| Q110 | - |  |  | SI | Age range(y) |
| Q111 | - |  |  | SI | Age range(y) |
| Q112 | - |  |  | SI | Upper Limit for Men |
| Q113 | - |  |  | SI | Upper Limit for Men |
| Q114 | - |  |  | SI | Upper Limit for Men |
| Q115 | - |  |  | SI | Upper Limit for Men |
| Q116 | - |  |  | SI | Upper Limit for Men |
| Q117 | - |  |  | SI | Upper Limit for Men |
| Q118 | - |  |  | SI | Upper Limit for Men |
| Q119 | - |  |  | SI | Upper Limit for Women |
| Q12 | - |  |  | SI | Cutoff determinant |
| Q120 | - |  |  | SI | Upper Limit for Women |
| Q121 | - |  |  | SI | Upper Limit for Women |
| Q122 | - |  |  | SI | Upper Limit for Women |
| Q123 | - |  |  | SI | Upper Limit for Women |
| Q124 | - |  |  | SI | Upper Limit for Women |
| Q125 | - |  |  | SI | Upper Limit for Women |
| Q126 | - |  |  | SI | Cutoff determinant |
| Q127 | - |  |  | SI | Cutoff determinant |
| Q128 | - |  |  | SI | Cutoff determinant |
| Q129 | - |  |  | SI | Cutoff determinant |
| Q13 | - |  |  | SI | End-point |
| Q130 | - |  |  | SI | Cutoff determinant |
| Q131 | - |  |  | SI | Cutoff determinant |
| Q132 | - |  |  | SI | Cutoff determinant |
| Q133 | - |  |  | SI | End-point |
| Q134 | - |  |  | SI | End-point |
| Q135 | - |  |  | SI | End-point |
| Q136 | - |  |  | SI | End-point |
| Q137 | - |  |  | SI | End-point |
| Q138 | - |  |  | SI | End-point |
| Q139 | - |  |  | SI | End-point |
| Q14 | - |  |  | SI | Ref |
| Q140 | - |  |  | SI | Ref |
| Q141 | - |  |  | SI | Ref |
| Q142 | - |  |  | SI | Ref |
| Q143 | - |  |  | SI | Ref |
| Q144 | - |  |  | SI | Ref |
| Q145 | - |  |  | SI | Ref |
| Q146 | - |  |  | SI | Ref |
| Q147 | - |  |  | SI | Ref |
| Q15 | - |  |  | SI | Northern Iran |
| Q16 | - |  |  | SI | 5,511 |
| Q17 | - |  |  | SI | ≥18 |
| Q18 | - |  |  | SI | 2.0 |
| Q19 | - |  |  | SI | 2.5 |
| Q20 | - |  |  | SI | Youden index |
| Q21 | - |  |  | SI | Metabolic Syndrome |
| Q22 | - |  |  | SI | 1 |
| Q23 | - |  |  | SI | Sweden |
| Q24 | - |  |  | SI | 4,816 |
| Q25 | - |  |  | SI | 50 to 74 |
| Q26 | - |  |  | SI | 2.0 |
| Q27 | - |  |  | SI | 2.0 |
| Q28 | - |  |  | SI | 75th centile |
| Q29 | - |  |  | SI | - |
| Q30 | - |  |  | SI | 2 |
| Q31 | - |  |  | SI | USA |
| Q32 | - |  |  | SI | 2,804 |
| Q33 | - |  |  | SI | ? |
| Q34 | - |  |  | SI | 2.73 |
| Q35 | - |  |  | SI | 2.73 |
| Q36 | - |  |  | SI | 66th centile |
| Q37 | - |  |  | SI | - |
| Q38 | - |  |  | SI | 3 |
| Q39 | - |  |  | SI | Chinese |
| Q40 | - |  |  | SI | 2,649 |
| Q41 | - |  |  | SI | 25 to 74 |
| Q42 | - |  |  | SI | 1.97 |
| Q43 | - |  |  | SI | 1.97 |
| Q44 | - |  |  | SI | Youden index |
| Q45 | - |  |  | SI | T2DM |
| Q46 | - |  |  | SI | 4 |
| Q47 | - |  |  | SI | Spain |
| Q48 | - |  |  | SI | 2,459 |
| Q49 | - |  |  | SI | 20 to 92 |
| Q50 | - |  |  | SI | 1.85 |
| Q51 | - |  |  | SI | 2.07 to 2.47* |
| Q52 | - |  |  | SI | Youden index |
| Q53 | - |  |  | SI | Metabolic syndrome |
| Q54 | - |  |  | SI | 5 |
| Q55 | - |  |  | SI | Japanese |
| Q56 | - |  |  | SI | 2,173 |
| Q57 | - |  |  | SI | 20 to 79 |
| Q58 | - |  |  | SI | 2.4 |
| Q59 | - |  |  | SI | 2.4 |
| Q60 | - |  |  | SI | 95th centile |
| Q61 | - |  |  | SI | - |
| Q62 | - |  |  | SI | 6 |
| Q63 | - |  |  | SI | Italy |
| Q64 | - |  |  | SI | 225 |
| Q65 | - |  |  | SI | 40 to 79 |
| Q66 | - |  |  | SI | 2.77 |
| Q67 | - |  |  | SI | 2.77 |
| Q68 | - |  |  | SI | 80th centile |
| Q69 | - |  |  | SI | - |
| Q70 | - |  |  | SI | 7 |
| Q71 | - |  |  | SI | T2DM, Type 2 diabetes mellitus. |
| Q72 | - |  |  | SI | *, Depending on age. |
| Q73 | - |  |  | SI | References |
| Q74 | - |  |  | SI | 1. Motamed N, Miresmail SJ, Rabiee B, Keyvani H, F... |
| Q75 | - |  |  | SI | A population based study. Journal of diabetes and ... |
| Q76 | - |  |  | SI | 2. Hedblad B, Nilsson P, Janzon L, Berglund G. Rel... |
| Q77 | - |  |  | SI | Results from a cross‐sectional study in Malmö, Swe... |
| Q78 | - |  |  | SI | 3. Sumner AE, Cowie CC. Ethnic differences in the ... |
| Q79 | - |  |  | SI | 4. Lee CH, Shih AZ, Woo YC, Fong CH, Leung OY, Jan... |
| Q80 | - |  |  | SI | Optimal cut-offs of homeostasis model assessment o... |
| Q81 | - |  |  | SI | 5. Gayoso-Diz P, Otero-González A, Rodriguez-Alvar... |
| Q82 | - |  |  | SI | Insulin resistance (HOMA-IR) cut-off values and th... |
| Q83 | - |  |  | SI | 6. Yamada C, Mitsuhashi T, Hiratsuka N, Inabe F, A... |
| Q84 | - |  |  | SI | Optimal reference interval for homeostasis model a... |
| Q85 | - |  |  | SI | 7. Bonora E, Kiechl S, Willeit J, Oberhollenzer F,... |
| Q86 | - |  |  | SI | the Bruneck Study. Diabetes. 1998 Oct 1 |
| Q87 | - |  |  | SI | Please check the guidelines. |
| Q88 | - |  |  | SI | Date |
| Q89 | - |  |  | SI | Time |
| Q90 | - |  |  | SI | The HOMA-IR (Homeostatic Model Assessment of Insul... |
| Q91 | - |  |  | SI | Population |
| Q92 | - |  |  | SI | Population |
| Q93 | - |  |  | SI | Population |
| Q94 | - |  |  | SI | Population |
| Q95 | - |  |  | SI | Population |
| Q96 | - |  |  | SI | Population |
| Q97 | - |  |  | SI | Population |
| Q98 | - |  |  | SI | n |
| Q99 | - |  |  | SI | n |
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