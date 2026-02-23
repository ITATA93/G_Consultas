# SQLUser.CT_CareProv

**Schema:** SQLUser
**Columnas:** 167
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPCP_RowId1 | varchar | PK |  | NO | - |
| CTPCP_Acceptance | varchar |  |  | SI | Acceptance |
| CTPCP_ActiveFlag | varchar |  |  | NO | ActiveFlag |
| CTPCP_AddrType_DR | bigint |  | FK | SI | Des Ref to CTADR |
| CTPCP_AdmittingRights | varchar |  |  | SI | AdmittingRights |
| CTPCP_AllocatedDoctor | varchar |  |  | SI | Allocated Doctor |
| CTPCP_Anaesthetist | varchar |  |  | SI | Anaesthetist |
| CTPCP_AuthorID | varchar |  |  | SI | Author ID |
| CTPCP_BestContactTime | varchar |  |  | SI | Best Contact Time |
| CTPCP_Blk | varchar |  |  | SI | Address Block Number |
| CTPCP_CPGroupAffiliations | varchar |  |  | SI | Affilations as List of Care Provider Groups |
| CTPCP_CPGroup_DR | bigint |  | FK | SI | Des Ref CPGroup |
| CTPCP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| CTPCP_CarPrvTp_DR | bigint |  | FK | NO | Des Ref to CTCPT |
| CTPCP_Category | varchar |  |  | SI | Care Provider Category |
| CTPCP_City_DR | bigint |  | FK | SI | Des Ref to CTCIT |
| CTPCP_Code | varchar |  |  | NO | Care Provider Code |
| CTPCP_CodeTranslated | varchar |  |  | SI | - |
| CTPCP_Con1Code_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| CTPCP_Con2Code_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| CTPCP_ConfidentialFax | varchar |  |  | SI | Confidential Fax Number |
| CTPCP_ContactFirstOn | varchar |  |  | SI | Contact First On |
| CTPCP_Continuing | varchar |  |  | SI | Continuing |
| CTPCP_CourierCopies | numeric |  |  | SI | Deprecated
The default number of copies of Lab Do... |
| CTPCP_Courier_DR | bigint |  | FK | SI | Deprecated
The default Courier to use for Lab Doc... |
| CTPCP_CreatedDate | date |  |  | SI | CreatedDate |
| CTPCP_CreatedHosp_DR | bigint |  | FK | SI | Des Ref CreatedHosp |
| CTPCP_CreatedTime | time |  |  | SI | CreatedTime |
| CTPCP_CreatedUser_DR | bigint |  | FK | SI | Des Ref CreatedUser |
| CTPCP_CumulativeEpisodes | integer |  |  | SI | Deprecated
Cumulatives Maximum Number of Episodes... |
| CTPCP_CumulativeOrder | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Order
The ... |
| CTPCP_CumulativePreference | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Preference... |
| CTPCP_DOB | varchar |  |  | SI | Date Of Birth |
| CTPCP_DateActiveFrom | date |  |  | NO | Date Active From |
| CTPCP_DateActiveTo | date |  |  | SI | Date Active To |
| CTPCP_DeactivationReason | varchar |  |  | SI | Deactivation reason |
| CTPCP_Desc | varchar |  |  | NO | Care Provider Name |
| CTPCP_DescTranslated | varchar |  |  | SI | - |
| CTPCP_DoctorsReportsDeliverySort | varchar |  |  | SI | Deprecated
Doctors Reports Delivery Sort
The sor... |
| CTPCP_DoctorsReportsTo | varchar |  |  | SI | Deprecated
A switch determining the default recip... |
| CTPCP_DoctorsReportsType | varchar |  |  | SI | Deprecated
The report type to use for doctors rep... |
| CTPCP_Email | varchar |  |  | SI | Email |
| CTPCP_ExternalCareProv | varchar |  |  | SI | External Care Provider |
| CTPCP_ExternalInterfaceQueue_DR | bigint |  | FK | SI | Deprecated
External Interface Queue |
| CTPCP_Fax | varchar |  |  | SI | Fax Number |
| CTPCP_FirstDigitInQueue | varchar |  |  | SI | First Digit of the Queue Number |
| CTPCP_FirstName | varchar |  |  | SI | First Name |
| CTPCP_HICApproved | varchar |  |  | SI | HICApproved |
| CTPCP_Hosp_DR | bigint |  | FK | SI | Des Ref to CTRFC |
| CTPCP_Id | varchar |  |  | SI | Care Provider Id |
| CTPCP_Language_DR | bigint |  | FK | SI | Deprecated
Doctors Reports Language
The language... |
| CTPCP_Level | varchar |  |  | SI | Address Building Level |
| CTPCP_LinkDoctor_DR | varchar |  | FK | SI | Des REf Link Doctor |
| CTPCP_MailList | varchar |  |  | SI | Mail List |
| CTPCP_MantouxTest | varchar |  |  | SI | MantouxTest |
| CTPCP_ManualPrint | varchar |  |  | SI | Deprecated
Manual Print
Flag to show if Doctors ... |
| CTPCP_MobilePhone | varchar |  |  | SI | Mobile Phone |
| CTPCP_Nation_DR | bigint |  | FK | SI | Des Ref to CTNAT |
| CTPCP_New | varchar |  |  | SI | New |
| CTPCP_OTConsultant | varchar |  |  | SI | OT Consultant (owner) |
| CTPCP_OtherLanguage_DR | bigint |  | FK | SI | Des Ref PrefLanguage |
| CTPCP_OtherName | varchar |  |  | SI | Other Name |
| CTPCP_PBSProviderType | varchar |  |  | SI | The Type of PBS Provider |
| CTPCP_PagerNo | varchar |  |  | SI | Pager Number |
| CTPCP_PathologySelfDetermine | varchar |  |  | SI | Pathology Self Determine |
| CTPCP_PractitionerFlag1 | varchar |  |  | SI | Practitioner Flag1 |
| CTPCP_PrefConMethod | varchar |  |  | SI | Preferred Contact Method |
| CTPCP_PrefLanguage_DR | bigint |  | FK | SI | Des Ref PrefLanguage |
| CTPCP_PrefMailAddFlad | varchar |  |  | SI | PrefMailAddFlad |
| CTPCP_PrescriberNumber | varchar |  |  | SI | Prescriber Number |
| CTPCP_Previous | varchar |  |  | SI | Previous |
| CTPCP_Province_DR | bigint |  | FK | SI | Province |
| CTPCP_QuickPrint | varchar |  |  | SI | Deprecated
The default Quick-Print flag for Docto... |
| CTPCP_Radiologist | varchar |  |  | SI | Radiologist |
| CTPCP_ReferralDoctor_DR | bigint |  | FK | SI | Des Ref ReferralDoctor |
| CTPCP_RegIssuer | bigint |  |  | SI | Professional Registration Issuer |
| CTPCP_Region_DR | bigint |  | FK | SI | Region |
| CTPCP_ReportMode | varchar |  |  | SI | Deprecated
Report Mode |
| CTPCP_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| CTPCP_RowId | varchar |  |  | NO | CTPCP Row ID |
| CTPCP_SMCNo | varchar |  |  | SI | Doctor SMC Number |
| CTPCP_SecondaryPrescriberNumber | varchar |  |  | SI | The Secondary Prescriber Number - used in AU regio... |
| CTPCP_Sex_DR | bigint |  | FK | SI | Des Ref to CTSEX |
| CTPCP_Signature | longvarbinary |  |  | SI | Signature as BinaryStream |
| CTPCP_Spec_DR | bigint |  | FK | SI | Des Ref to CTSPC |
| CTPCP_SpecialistYN | varchar |  |  | SI | Specialist Y/N |
| CTPCP_SpecstPalliativeCP | varchar |  |  | SI | SpecstPalliativeCP |
| CTPCP_StName | varchar |  |  | SI | Address Street Name |
| CTPCP_State_DR | bigint |  | FK | SI | Des Ref to CTSTT |
| CTPCP_SubSpec_DR | bigint |  | FK | SI | Des Ref to CTSPC |
| CTPCP_Surgeon | varchar |  |  | SI | Surgeon |
| CTPCP_Surname | varchar |  |  | SI | Surname |
| CTPCP_TelH | varchar |  |  | SI | Home Telephone Number |
| CTPCP_TelO | varchar |  |  | SI | Office Telephone Number |
| CTPCP_TelOExt | varchar |  |  | SI | Office Telephone Extension |
| CTPCP_TextField | varchar |  |  | SI | Generic free text field for Care Provider |
| CTPCP_TextOne | varchar |  |  | SI | Text 1 |
| CTPCP_TextThree | varchar |  |  | SI | TextThree |
| CTPCP_TextTitle | varchar |  |  | SI | TextThree |
| CTPCP_TextTwo | varchar |  |  | SI | Text 2 |
| CTPCP_Title | varchar |  |  | SI | Title |
| CTPCP_Title_DR | bigint |  | FK | SI | Des Ref Title |
| CTPCP_Unit | varchar |  |  | SI | Address Unit Number |
| CTPCP_UpdateDate | date |  |  | SI | UpdateDate |
| CTPCP_UpdateHosp_DR | bigint |  | FK | SI | Des Ref UpdateHosp |
| CTPCP_UpdateTime | time |  |  | SI | UpdateTime |
| CTPCP_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| CTPCP_UpdatedDate | date |  |  | SI | Updated Date |
| CTPCP_UpdatedTime | time |  |  | SI | Updated Time |
| CTPCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTPCP_VersionDate | date |  |  | SI | Effective Date |
| CTPCP_VersionDateTime | varchar |  |  | SI | Effective Date / Time |
| CTPCP_VersionNumber | double |  |  | SI | Version |
| CTPCP_VersionOrigin_DR | varchar |  | FK | SI | Des Ref to Original Version |
| CTPCP_VersionTime | time |  |  | SI | Effective Time |
| CTPCP_WLOutpatientRights | varchar |  |  | SI | WLOutpatientRights  |
| CTPCP_WLTriageRights | varchar |  |  | SI | WLTriageRights  |
| CTPCP_YesNo1 | varchar |  |  | SI | Generic Care Provider Checkbox 1 |
| CTPCP_YesNo2 | varchar |  |  | SI | Generic Care Provider Checkbox 2 |
| CTPCP_YesNo3 | varchar |  |  | SI | Generic Care Provider Checkbox 3 |
| CTPCP_YesNo4 | varchar |  |  | SI | Generic Care Provider Checkbox 4 |
| CTPCP_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP |
| Q01 | - |  |  | SI | Nombre Funcionario que Crea el Volumen |
| Q02 | - |  |  | SI | RUN Funcionario que Crea el Volumen |
| Q03 | - |  |  | SI | N° de Volumen |
| Q04 | - |  |  | SI | Fecha de Creación |
| Q05 | - |  |  | SI | Hora de Creación |
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