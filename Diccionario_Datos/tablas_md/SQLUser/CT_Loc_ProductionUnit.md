# SQLUser.CT_Loc_ProductionUnit

**Schema:** SQLUser
**Columnas:** 231
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRODUNIT_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| ChildQ37DR | - |  |  | SI | Child Reference: Anti D prophylaxis |
| PRODUNIT_ActivityCode | varchar |  |  | SI | Activity  Code |
| PRODUNIT_AdmReason_DR | bigint |  | FK | SI | Des Ref PACAdmReason |
| PRODUNIT_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxilInsurType |
| PRODUNIT_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| PRODUNIT_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| PRODUNIT_Childsub | double |  |  | NO | Childsub |
| PRODUNIT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRODUNIT_CreatedDate | date |  |  | SI | Created Date |
| PRODUNIT_CreatedTime | time |  |  | SI | Created Time |
| PRODUNIT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRODUNIT_DateFrom | date |  |  | NO | Date  From |
| PRODUNIT_DateTo | date |  |  | SI | Date To |
| PRODUNIT_EpisSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| PRODUNIT_EpisodeType | varchar |  |  | SI | Episode Type |
| PRODUNIT_GLCCC_DR | bigint |  | FK | SI | Des Ref GLCCC |
| PRODUNIT_InsType_DR | bigint |  | FK | SI | Des Ref to ARCInsuranceType |
| PRODUNIT_ItemCat_DR | bigint |  | FK | SI | Des Ref ItemCat |
| PRODUNIT_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| PRODUNIT_OrderCateg_DR | bigint |  | FK | SI | Des Ref OrderCategory |
| PRODUNIT_Rank | double |  |  | SI | Rank |
| PRODUNIT_ReportingType_DR | bigint |  | FK | SI | Des Ref PACReportingType |
| PRODUNIT_Resource_DR | bigint |  | FK | SI | Des Ref RBResource |
| PRODUNIT_RowId | varchar |  |  | NO | - |
| PRODUNIT_SerialNumberCode | varchar |  |  | SI | SerialNumber  Code |
| PRODUNIT_Text1 | varchar |  |  | SI | Text1 |
| PRODUNIT_Text2 | varchar |  |  | SI | Text2 |
| PRODUNIT_Text3 | varchar |  |  | SI | Text3 |
| PRODUNIT_Text4 | varchar |  |  | SI | Text4 |
| PRODUNIT_Text5 | varchar |  |  | SI | Text5 |
| PRODUNIT_UPCode | varchar |  |  | SI | UP Code |
| PRODUNIT_UpdatedDate | date |  |  | SI | Updated Date |
| PRODUNIT_UpdatedTime | time |  |  | SI | Updated Time |
| PRODUNIT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PRODUNIT_YesNo1 | varchar |  |  | SI | YesNo1 |
| PRODUNIT_YesNo2 | varchar |  |  | SI | YesNo2 |
| PRODUNIT_YesNo3 | varchar |  |  | SI | YesNo3 |
| PRODUNIT_YesNo4 | varchar |  |  | SI | YesNo4 |
| PRODUNIT_YesNo5 | varchar |  |  | SI | YesNo5 |
| Q01 | - |  |  | SI | Spina bifida |
| Q01A | - |  |  | SI | Spina bifida explained |
| Q01B | - |  |  | SI | Spina bifida accepted |
| Q01C | - |  |  | SI | Spina bifida date due/taken |
| Q01D | - |  |  | SI | Spina bifida result date |
| Q01E | - |  |  | SI | Spina bifida result |
| Q02 | - |  |  | SI | Down's syndrome |
| Q02A | - |  |  | SI | Down's syndrome explained |
| Q02B | - |  |  | SI | Down's syndrome accepted |
| Q02C | - |  |  | SI | Down's syndrome date due/taken |
| Q02D | - |  |  | SI | Down's syndrome result date |
| Q02E | - |  |  | SI | Down's syndrome result |
| Q03 | - |  |  | SI | Edward's syndrome |
| Q03A | - |  |  | SI | Edward's syndrome explained |
| Q03B | - |  |  | SI | Edward's syndrome accepted |
| Q03C | - |  |  | SI | Edward's syndrome date due/taken |
| Q03D | - |  |  | SI | Edward's syndrome result date |
| Q03E | - |  |  | SI | Edward's syndrome result |
| Q04 | - |  |  | SI | Chlamydia |
| Q04A | - |  |  | SI | Chlamydia explained |
| Q04B | - |  |  | SI | Chlamydia accepted |
| Q04C | - |  |  | SI | Chlamydia date due/taken |
| Q04D | - |  |  | SI | Chlamydia result date |
| Q04E | - |  |  | SI | Chlamydia result |
| Q05 | - |  |  | SI | Haemoglobinopathy |
| Q05A | - |  |  | SI | Haemoglobinopathy explained |
| Q05B | - |  |  | SI | Haemoglobinopathy accepted |
| Q05C | - |  |  | SI | Haemoglobinopathy date due/taken |
| Q05D | - |  |  | SI | Haemoglobinopathy result date |
| Q05E | - |  |  | SI | Haemoglobinopathy result |
| Q06 | - |  |  | SI | MSU |
| Q06A | - |  |  | SI | MSU explained |
| Q06B | - |  |  | SI | MSU accepted |
| Q06C | - |  |  | SI | MSU date due/taken |
| Q06D | - |  |  | SI | MSU result date |
| Q06E | - |  |  | SI | MSU result |
| Q07 | - |  |  | SI | Blood group |
| Q07A | - |  |  | SI | Blood group explained |
| Q07B | - |  |  | SI | Blood group accepted |
| Q07C | - |  |  | SI | Blood group date due/taken |
| Q07D | - |  |  | SI | Blood group result date |
| Q07E | - |  |  | SI | Blood group result |
| Q08 | - |  |  | SI | Antibodies |
| Q08A | - |  |  | SI | Antibodies explained |
| Q08B | - |  |  | SI | Antibodies accepted |
| Q08C | - |  |  | SI | Antibodies date due/taken |
| Q08D | - |  |  | SI | Antibodies result date |
| Q08E | - |  |  | SI | Antibodies result |
| Q09 | - |  |  | SI | Sickle cell |
| Q09A | - |  |  | SI | Sickle cell explained |
| Q09B | - |  |  | SI | Sickle cell accepted |
| Q09C | - |  |  | SI | Sickle cell date due/taken |
| Q09D | - |  |  | SI | Sickle cell result date |
| Q09E | - |  |  | SI | Sickle cell result |
| Q10 | - |  |  | SI | Thallassaemia |
| Q10A | - |  |  | SI | Thalassaemia explained |
| Q10B | - |  |  | SI | Thalassaemia accepted |
| Q10C | - |  |  | SI | Thalassaemia date due/taken |
| Q10D | - |  |  | SI | Thalassaemia result date |
| Q10E | - |  |  | SI | Thalassaemia result |
| Q11 | - |  |  | SI | Rubella |
| Q11A | - |  |  | SI | Rubella explained |
| Q11B | - |  |  | SI | Rubella accepted |
| Q11C | - |  |  | SI | Rubella date due/taken |
| Q11D | - |  |  | SI | Rubella result date |
| Q11E | - |  |  | SI | Rubella result |
| Q12 | - |  |  | SI | Hepatitis B |
| Q12A | - |  |  | SI | Hepatitis B explained |
| Q12B | - |  |  | SI | Hepatitis B accepted |
| Q12C | - |  |  | SI | Hepatitis B date due/taken |
| Q12D | - |  |  | SI | Hepatitis B result date |
| Q12E | - |  |  | SI | Hepatitis B result |
| Q13 | - |  |  | SI | Syphilis |
| Q134 | - |  |  | SI | Repeat blood group |
| Q135 | - |  |  | SI | Repeat blood group explained |
| Q136 | - |  |  | SI | Repeat blood group accepted |
| Q137 | - |  |  | SI | Repeat blood group date due/taken |
| Q138 | - |  |  | SI | Repeat blood group result date |
| Q139 | - |  |  | SI | Repeat blood group result |
| Q13A | - |  |  | SI | Syphilis explained |
| Q13B | - |  |  | SI | Syphilis accepted |
| Q13C | - |  |  | SI | Syphilis date due/taken |
| Q13D | - |  |  | SI | Syphilis result date |
| Q13E | - |  |  | SI | Syphilis result |
| Q14 | - |  |  | SI | HIV |
| Q140 | - |  |  | SI | Repeat FBC |
| Q141 | - |  |  | SI | Repeat FBC explained |
| Q142 | - |  |  | SI | Repeat FBC accepted |
| Q143 | - |  |  | SI | Repeat FBC date due/taken |
| Q144 | - |  |  | SI | Repeat FBC result date |
| Q145 | - |  |  | SI | Repeat FBC result |
| Q146 | - |  |  | SI | Repeat blood glucose |
| Q147 | - |  |  | SI | Repeat blood glucose explained |
| Q148 | - |  |  | SI | Repeat blood glucose accepted |
| Q149 | - |  |  | SI | Repeat blood glucose date due/taken |
| Q14A | - |  |  | SI | HIV explained |
| Q14B | - |  |  | SI | HIV accepted |
| Q14C | - |  |  | SI | HIV date due/taken |
| Q14D | - |  |  | SI | HIV result date |
| Q14E | - |  |  | SI | HIV result |
| Q15 | - |  |  | SI | Platelets |
| Q150 | - |  |  | SI | Repeat blood glucose result date |
| Q151 | - |  |  | SI | Repeat blood glucose result |
| Q152 | - |  |  | SI | Antenatal tests and investigations |
| Q16 | - |  |  | SI | Bile acid |
| Q17 | - |  |  | SI | Cross match |
| Q18 | - |  |  | SI | Kleihauer |
| Q19 | - |  |  | SI | Maternal serum |
| Q2 | - |  |  | SI | Liver function tests |
| Q20 | - |  |  | SI | Thyroid function test |
| Q21 | - |  |  | SI | Toxoplasmosis |
| Q22 | - |  |  | SI | Urea and Electrolytes |
| Q23 | - |  |  | SI | Full blood count |
| Q24 | - |  |  | SI | Clotting studies |
| Q26 | - |  |  | SI | HbA1c |
| Q28 | - |  |  | SI | TORCH screen |
| Q29 | - |  |  | SI | Urates |
| Q30 | - |  |  | SI | Other |
| Q31 | - |  |  | SI | Details |
| Q32 | - |  |  | SI | MRSA |
| Q32A | - |  |  | SI | MRSA explained |
| Q32B | - |  |  | SI | MRSA accepted |
| Q32C | - |  |  | SI | MRSA date due/taken |
| Q32D | - |  |  | SI | MRSA result date |
| Q32E | - |  |  | SI | MRSA result |
| Q33 | - |  |  | SI | OGTT |
| Q33A | - |  |  | SI | OGTT explained |
| Q33B | - |  |  | SI | OGTT accepted |
| Q33C | - |  |  | SI | OGTT date due/taken |
| Q33D | - |  |  | SI | OGTT result date |
| Q33E | - |  |  | SI | OGTT result |
| Q34 | - |  |  | SI | Repeat Haemoglobinopathy |
| Q34A | - |  |  | SI | Repeat Haemoglobinopathy explained |
| Q34B | - |  |  | SI | Repeat Haemoglobinopathy accepted |
| Q34C | - |  |  | SI | Repeat Haemoglobinopathy date due/taken |
| Q34D | - |  |  | SI | Repeat Haemoglobinopathy result date |
| Q34E | - |  |  | SI | Repeat Haemoglobinopathy result |
| Q35 | - |  |  | SI | Repeat Antibodies |
| Q35A | - |  |  | SI | Repeat Antibodies explained |
| Q35B | - |  |  | SI | Repeat Antibodies accepted |
| Q35C | - |  |  | SI | Repeat Antibodies date due/taken |
| Q35D | - |  |  | SI | Repeat Antibodies result date |
| Q35E | - |  |  | SI | Repeat Antibodies result |
| Q36 | - |  |  | SI | Asymptomatic Bacteriuria |
| Q36A | - |  |  | SI | Asymptomatic Bacteriuria explained |
| Q36B | - |  |  | SI | Asymptomatic Bacteriuria accepted |
| Q36C | - |  |  | SI | Asymptomatic Bacteriuria date due/taken |
| Q36D | - |  |  | SI | Asymptomatic Bacteriuria result date |
| Q36E | - |  |  | SI | Asymptomatic Bacteriuria result |
| Q38 | - |  |  | SI | Which tests were declined and why |
| Q39 | - |  |  | SI | Actions |
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