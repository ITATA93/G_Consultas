# SQLUser.PA_PregDelivery

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEL_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| DEL_Adm_DR | bigint |  | FK | SI | Des ref PA_ADM |
| DEL_AnaestPostDelivery_DR | bigint |  | FK | SI | Des Ref ORCAnaesthesiaDuringDelivery |
| DEL_AnaestPreDelivery_DR | bigint |  | FK | SI | Des Ref ORCAnaesthesiaDuringDelivery |
| DEL_AnaesthesiaForAbortionText | varchar |  |  | SI | Anaesthesia for Abortion free text |
| DEL_AnaesthesiaForAbortion_DR | bigint |  | FK | SI | Des Ref ORCAnaesthesiaDuringDelivery |
| DEL_Analgetics_DR | bigint |  | FK | SI | Des Ref Analgetics |
| DEL_AntenatalSteroids_DR | bigint |  | FK | SI | Des Ref PAC_AntenatalSteroid |
| DEL_AuscultationBCF_DR | bigint |  | FK | SI | Des Ref ORCAuscultationBCF |
| DEL_BloodLoss | double |  |  | SI | Blood Loss  |
| DEL_BloodTransfusion | varchar |  |  | SI | Blood Transfusion |
| DEL_Cardiotocography_DR | bigint |  | FK | SI | Des Ref ORCCardiotocography |
| DEL_CertificationAuthoriser_DR | bigint |  | FK | SI | Des Ref ORCCertificationAuthoriser |
| DEL_CertificationDate | date |  |  | SI | Date of Certification |
| DEL_CervixDilation | double |  |  | SI | Cervix Dilation  |
| DEL_Childsub | double |  |  | NO | Childsub |
| DEL_Comments | varchar |  |  | SI | Comments |
| DEL_ContractionsInterval | double |  |  | SI | Contractions Interval |
| DEL_CsDecisionDate | date |  |  | SI | Caesarean decision date |
| DEL_CsDecisionTime | time |  |  | SI | CS Decision Time |
| DEL_DateHindWaterLeak | date |  |  | SI | Date of Hind Water Leak |
| DEL_DateOfInduction | date |  |  | SI | Date of Induction |
| DEL_DateofAugtm | date |  |  | SI | DateofAugtm |
| DEL_DegreeLaceration_DR | bigint |  | FK | SI | Degree of Laceration |
| DEL_DeliveryType | varchar |  |  | SI | Delivery Type |
| DEL_DrugAndDoseOfAntibiotic | varchar |  |  | SI | Drug and Dose of Antibiotic |
| DEL_EpisType_DR | bigint |  | FK | SI | Des Ref Episiotomy Type |
| DEL_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| DEL_ExpulsionStartDate | date |  |  | SI | Expulsion Start Date |
| DEL_ExpulsionStartTime | time |  |  | SI | Expulsion Start Time |
| DEL_FreeText1 | varchar |  |  | SI | FreeText1 |
| DEL_FreeText2 | varchar |  |  | SI | FreeText2 |
| DEL_FreeText3 | varchar |  |  | SI | FreeText3 |
| DEL_FullDilatationDate | date |  |  | SI | Full Dilatation Date |
| DEL_FullDilatationTime | time |  |  | SI | Full Dilatation Time |
| DEL_IVAntibDuringDeliv_DR | bigint |  | FK | SI | Des Ref ORCIVAntibioticDuringDelivery |
| DEL_InstrTrackDone | varchar |  |  | SI | Instruments tracking done |
| DEL_LabDelPrefMet | varchar |  |  | SI | Labour & Delivery Preferences Met |
| DEL_LabourCareType_DR | bigint |  | FK | SI | Des Ref PAC_MaternityType |
| DEL_LabourMethod_DR | bigint |  | FK | SI | Labour Method |
| DEL_LabourOnsetDate | date |  |  | SI | Labour Onset Date |
| DEL_LabourOnsetTime | time |  |  | SI | Labour Onset Time |
| DEL_LiquorColour_DR | bigint |  | FK | SI | Des Ref PACLiquorColour |
| DEL_MagSulphateAdmin | varchar |  |  | SI | Magnesium Sulphate administered  |
| DEL_MaternalPosition_DR | bigint |  | FK | SI | Des Ref PACMaternalPosition |
| DEL_MaternalRefus_DR | bigint |  | FK | SI | Des Ref MaternalRefus |
| DEL_MembRuptureDate | date |  |  | SI | MembRuptureDate |
| DEL_MembRuptureDuration | varchar |  |  | SI | MembRuptureDuration |
| DEL_MembRuptureTime | time |  |  | SI | MembRuptureTime |
| DEL_MembRuptureType_DR | bigint |  | FK | SI | Type of Membrane Rupture |
| DEL_MidwifeCareInLabour | varchar |  |  | SI | Midwife Care in Labour  |
| DEL_MidwifeCareTeam_DR | bigint |  | FK | SI | Midwife Care Team |
| DEL_MidwifeConsultTrnsfr_DR | bigint |  | FK | SI | Des ref PAC_MidwifeToConsTrans |
| DEL_MinorAgreemAuthoriser_DR | bigint |  | FK | SI | Des Ref ORCMinorAgreemAuthoriser |
| DEL_MostSeniorDoc_DR | bigint |  | FK | SI | Most senior doctor Des Ref  CT_CarPrv |
| DEL_MostSeniorMidwife_DR | bigint |  | FK | SI | Most senior midwife Des Ref CT_CarPrvTp |
| DEL_MotherOutcome_DR | bigint |  | FK | SI | Des Ref PAC_MotherOutcome |
| DEL_Num_Sutures | double |  |  | SI | Num_Sutures |
| DEL_OthIndAugMthd | varchar |  |  | SI | Other Induction Augmentation methods |
| DEL_OthIndIndctr | varchar |  |  | SI | Other Induction Indicators |
| DEL_OthLabDelCompl | varchar |  |  | SI | Other Labour & Delivery Complications |
| DEL_OthPuerpCompl | varchar |  |  | SI | Other puerperium complications |
| DEL_PainReliefFreeText | varchar |  |  | SI | PainReliefFreeText |
| DEL_Partograms_DR | bigint |  | FK | SI | Des Ref ORCPartograms |
| DEL_PerinealRepair | varchar |  |  | SI | Perineal Repair Undertaken |
| DEL_PerineumText | varchar |  |  | SI | Perineum free text |
| DEL_Perineum_DR | bigint |  | FK | SI | Des ref PAC_Perineum |
| DEL_PlannedInductionMth_DR | bigint |  | FK | SI | Des Ref PAC_IndcutionMethods |
| DEL_Plurality | bigint |  |  | SI | Plurality |
| DEL_PregDiabTreat_DR | bigint |  | FK | SI | Diabetes Treatment During Pregnancy |
| DEL_PrematRuptureMembrane | varchar |  |  | SI | Premature Rupture of the memberanes |
| DEL_QuantityOfInductDrug | double |  |  | SI | Quantity of Induction Drug |
| DEL_RowId | varchar |  |  | NO | - |
| DEL_SkinClosure_DR | bigint |  | FK | SI | Des Ref PAC_SkinClosure |
| DEL_SmokingDuringPreg_DR | bigint |  | FK | SI | Des Ref PAC_SmokerDuringPregn |
| DEL_Stage1 | varchar |  |  | SI | Duration of Stage 1 |
| DEL_Stage2 | varchar |  |  | SI | Duration of Stage 2 |
| DEL_Stage3 | varchar |  |  | SI | Duration of Stage 3 |
| DEL_SterileAfterDelivery | varchar |  |  | SI | Sterile after delivery |
| DEL_SutureBy | varchar |  |  | SI | Des Ref CT_CareProv |
| DEL_SutureType | bigint |  |  | SI | Des Ref PAC_SutureType |
| DEL_Sutures_Super_DR | varchar |  | FK | SI | Des Ref Sutures_Super |
| DEL_Text1 | varchar |  |  | SI | Text1 |
| DEL_Text2 | varchar |  |  | SI | Text2 |
| DEL_Text3 | varchar |  |  | SI | Text3 |
| DEL_Text4 | varchar |  |  | SI | Text4 |
| DEL_Text5 | varchar |  |  | SI | Text5 |
| DEL_Text6 | varchar |  |  | SI | Text6 |
| DEL_Text7 | varchar |  |  | SI | Text7 |
| DEL_Text8 | varchar |  |  | SI | Text8 |
| DEL_TimeHindWaterLeak | time |  |  | SI | Time of Hind Water Leak |
| DEL_TimeOfInduction | time |  |  | SI | Time of Induction |
| DEL_TimeofAugtm | time |  |  | SI | TimeofAugtm |
| DEL_TotalDuration | varchar |  |  | SI | Duration of labour |
| DEL_TypeOfAbortionText | varchar |  |  | SI | Type of abortion free text |
| DEL_TypeOfAbortion_DR | bigint |  | FK | SI | Des ref PAC_TypeOfAbortion |
| DEL_UOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| DEL_UpdateDate | date |  |  | SI | Last Update Date |
| DEL_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| DEL_UpdateTime | time |  |  | SI | Last update time |
| DEL_UpdateUser | bigint |  |  | SI | Last Update User |
| DEL_Urgent | varchar |  |  | SI | Urgent |
| DEL_YesNo1 | varchar |  |  | SI | YesNo1 |
| DEL_YesNo10 | varchar |  |  | SI | YesNo10 |
| DEL_YesNo2 | varchar |  |  | SI | YesNo2 |
| DEL_YesNo3 | varchar |  |  | SI | YesNo3 |
| DEL_YesNo4 | varchar |  |  | SI | YesNo4 |
| DEL_YesNo5 | varchar |  |  | SI | YesNo5 |
| DEL_YesNo6 | varchar |  |  | SI | YesNo6 |
| DEL_YesNo7 | varchar |  |  | SI | YesNo7 |
| DEL_YesNo8 | varchar |  |  | SI | YesNo8 |
| DEL_YesNo9 | varchar |  |  | SI | YesNo9 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*