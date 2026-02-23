# SQLUser.OEC_OrderCategory

**Schema:** SQLUser
**Columnas:** 387
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORCAT_RowId | bigint | PK |  | NO | - |
| ORCAT_AddToDiagnosticStage | varchar |  |  | SI | Add to Diagnostic Stage |
| ORCAT_AllowQuestEditExecOrd | varchar |  |  | SI | Allow Questionnaire to be Edited for Executed Orde... |
| ORCAT_ApplyBatchPricing | varchar |  |  | SI | ApplyBatchPricing |
| ORCAT_AutoOrder | varchar |  |  | SI | Order Automatically from a Clinical Pathway |
| ORCAT_Code | varchar |  |  | NO | Code |
| ORCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORCAT_Commissioning | varchar |  |  | SI | Commissioning  |
| ORCAT_CounterTypeDR | bigint |  | FK | SI | Counter Type DR |
| ORCAT_CreatedDate | date |  |  | SI | Created Date |
| ORCAT_CreatedTime | time |  |  | SI | Created Time |
| ORCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORCAT_DateFrom | date |  |  | SI | DateFrom |
| ORCAT_DateTo | date |  |  | SI | DateTo |
| ORCAT_Desc | varchar |  |  | NO | Description |
| ORCAT_DiagnosticWaitTime | double |  |  | SI | DiagnosticWaitTime |
| ORCAT_DirectlyExecute | varchar |  |  | SI | Directly Execute from a Clinical Pathway |
| ORCAT_DisplayOPWhiteboard | varchar |  |  | SI | DisplayOPWhiteboard |
| ORCAT_DoNotDCOnAdmCancel | varchar |  |  | SI | Do Not D/C on Admission Cancel |
| ORCAT_DoNotDCOnAdmDisch | varchar |  |  | SI | Do not D/C on Admission Discharge |
| ORCAT_ExpiryDays | double |  |  | SI | ExpiryDays |
| ORCAT_FreqGroup_DR | bigint |  | FK | SI | Des Ref to OECFrequencyGroup |
| ORCAT_Hourly | varchar |  |  | SI | Hourly |
| ORCAT_HrsResultOverdue | double |  |  | SI | Hours Result Overdue |
| ORCAT_IVExpiry | double |  |  | SI | IV Expiry |
| ORCAT_IconApptsMade | varchar |  |  | SI | Icon to show Appointments made for order(s) |
| ORCAT_IconDisplayAfterExec | varchar |  |  | SI | Icon to Display After Execution |
| ORCAT_IconName | varchar |  |  | SI | Icon Name |
| ORCAT_IconPriority | varchar |  |  | SI | Icon Priority |
| ORCAT_IconResultOverdue | varchar |  |  | SI | Icon to show orders exceeded time ovdue resul |
| ORCAT_ImgAccssNoCnt_DR | bigint |  | FK | SI | des ref to PAC_CounterType |
| ORCAT_MarkReadyForInv | varchar |  |  | SI | MarkReadyForInv |
| ORCAT_NoShowIconAfterExcecut | varchar |  |  | SI | Don't Show Icon AfterExcecution |
| ORCAT_NonReviewable | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ORCAT_OCGroup_DR | bigint |  | FK | SI | Des Ref OCGroup |
| ORCAT_OrderSeqNo | double |  |  | SI | Order Sequence No |
| ORCAT_Owner | varchar |  |  | SI | Owner |
| ORCAT_PhoneOrderReviewTime | double |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ORCAT_PrescrExpDays | double |  |  | SI | PrescrExpDays |
| ORCAT_PrescrRepeatDays | double |  |  | SI | PrescrRepeatDays |
| ORCAT_Questionnaire_DR | bigint |  | FK | SI | Des Ref Questionnaire |
| ORCAT_RenderingTrigger | varchar |  |  | SI | Rendering Trigger |
| ORCAT_RepeatInOrder | varchar |  |  | NO | Repeat In Order |
| ORCAT_ReviewRequired | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2020+ (JRIA: T... |
| ORCAT_ShowIconBeforeEndDate | varchar |  |  | SI | Only Show Icon Before End Date |
| ORCAT_UpdatedDate | date |  |  | SI | Updated Date |
| ORCAT_UpdatedTime | time |  |  | SI | Updated Time |
| ORCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Sph-Rt |
| Q02 | - |  |  | SI | Sph-Lt |
| Q03 | - |  |  | SI | Axis-Rt |
| Q04 | - |  |  | SI | VA@Nr -OD |
| Q05 | - |  |  | SI | VA@Dt -OD |
| Q06 | - |  |  | SI | Sph-OD-WG |
| Q07 | - |  |  | SI | Cyl-Rt |
| Q08 | - |  |  | SI | Axis-Lt |
| Q09 | - |  |  | SI | VA@Nr -OS |
| Q10 | - |  |  | SI | VA@Dt -OS |
| Q100 | - |  |  | SI | Method 1 |
| Q101 | - |  |  | SI | Method 2 |
| Q102 | - |  |  | SI | Method 2 |
| Q103 | - |  |  | SI | Result |
| Q104 | - |  |  | SI | Result |
| Q105 | - |  |  | SI | Result |
| Q106 | - |  |  | SI | Method |
| Q107 | - |  |  | SI | OD |
| Q108 | - |  |  | SI | OS |
| Q109 | - |  |  | SI | OD |
| Q11 | - |  |  | SI | Sph-OS-WG |
| Q110 | - |  |  | SI | OS |
| Q111 | - |  |  | SI | Notes |
| Q112 | - |  |  | SI | Anesthetic used |
| Q113 | - |  |  | SI | OD |
| Q115 | - |  |  | SI | Cyl-OS-WG |
| Q116 | - |  |  | SI | OD Inferior Oblique |
| Q117 | - |  |  | SI | DRX-OD-Sph |
| Q118 | - |  |  | SI | DRX-OD-Cyl |
| Q119 | - |  |  | SI | VA-Nr-OSr |
| Q120 | - |  |  | SI | Notes |
| Q121 | - |  |  | SI | OS |
| Q125 | - |  |  | SI | Light & Accommodation |
| Q126 | - |  |  | SI | Notes |
| Q13 | - |  |  | SI | Cyl-Lt |
| Q131 | - |  |  | SI | Notes |
| Q133 | - |  |  | SI | Notes |
| Q137 | - |  |  | SI | Date |
| Q139 | - |  |  | SI | Cyl-OD-Wx |
| Q14 | - |  |  | SI | Cyl-OD-WG |
| Q140 | - |  |  | SI | Light & Accommodation |
| Q141 | - |  |  | SI | Reflex- Direct |
| Q142 | - |  |  | SI | Reflex- Direct |
| Q143 | - |  |  | SI | Reflex-Consensual |
| Q144 | - |  |  | SI | Reflex-Consensual |
| Q145 | - |  |  | SI | RAPD |
| Q146 | - |  |  | SI | RAPD |
| Q147 | - |  |  | SI | IOP-OD |
| Q147ObsDR | - |  |  | SI | IOP-OD DR |
| Q148 | - |  |  | SI | IOP-OS |
| Q148ObsDR | - |  |  | SI | IOP-OS DR |
| Q149 | - |  |  | SI | IOP-OD2 |
| Q149ObsDR | - |  |  | SI | IOP-OD2 DR |
| Q15 | - |  |  | SI | VA@Dt-UA-Rt |
| Q150 | - |  |  | SI | IOP-OS2 |
| Q150ObsDR | - |  |  | SI | IOP-OS2 DR |
| Q151 | - |  |  | SI | Gaze |
| Q152 | - |  |  | SI | OD |
| Q153 | - |  |  | SI | OS |
| Q154 | - |  |  | SI | Amsler Grid |
| Q155 | - |  |  | SI | Size |
| Q156 | - |  |  | SI | Axis-OD-WG |
| Q157 | - |  |  | SI | Axis-OS-WG |
| Q158 | - |  |  | SI | OD |
| Q159 | - |  |  | SI | OS |
| Q16 | - |  |  | SI | VA@Dt-UA-Lt |
| Q160 | - |  |  | SI | DRX-OD-Axis |
| Q161 | - |  |  | SI | DRX-OD-Add |
| Q162 | - |  |  | SI | DRX-OD-VADT |
| Q163 | - |  |  | SI | DRX-OD-VANR |
| Q164 | - |  |  | SI | DRX-OS-Sph |
| Q165 | - |  |  | SI | DRX-OS-Cyl |
| Q166 | - |  |  | SI | DRX-OS-Axis |
| Q167 | - |  |  | SI | DRX-OS-Add |
| Q168 | - |  |  | SI | DRX-OS-VADT |
| Q169 | - |  |  | SI | DRX-OS-VANR |
| Q17 | - |  |  | SI | VA@Nr-UA-Rt |
| Q170 | - |  |  | SI | DRX-OU-VADT |
| Q171 | - |  |  | SI | DRX-OU-VANR |
| Q172 | - |  |  | SI | Dynamic RX Notes |
| Q173 | - |  |  | SI | SRX-OD- Sph |
| Q174 | - |  |  | SI | SRX-OD- Cyl |
| Q175 | - |  |  | SI | SRX-OD- Axis |
| Q176 | - |  |  | SI | SRX-OD- Add |
| Q177 | - |  |  | SI | SRX-OD- VADT |
| Q178 | - |  |  | SI | SRX-OD- VANR |
| Q179 | - |  |  | SI | SRX-OS- Sph |
| Q18 | - |  |  | SI | VA@Nr-UA-Lt |
| Q180 | - |  |  | SI | SRX-OS- Cyl |
| Q181 | - |  |  | SI | SRX-OS- Axis |
| Q182 | - |  |  | SI | SRX-OS- Add |
| Q183 | - |  |  | SI | SRX-OS- VADT |
| Q184 | - |  |  | SI | SRX-OS- VANR |
| Q185 | - |  |  | SI | SRX-OU- VADT |
| Q186 | - |  |  | SI | SRX-OU- VANR |
| Q187 | - |  |  | SI | Statix Rx Notes |
| Q188 | - |  |  | SI | SRX- Informed Consent |
| Q189 | - |  |  | SI | VA - Dt |
| Q19 | - |  |  | SI | Add-OD-Fx |
| Q190 | - |  |  | SI | Shape |
| Q191 | - |  |  | SI | Biomicroscopy Right Eye |
| Q192 | - |  |  | SI | Biomicroscopy left Eye |
| Q193 | - |  |  | SI | PS Right Eye |
| Q194 | - |  |  | SI | PS Left Eye |
| Q195 | - |  |  | SI | Sph |
| Q196 | - |  |  | SI | Cyl |
| Q197 | - |  |  | SI | Axis |
| Q198 | - |  |  | SI | Add |
| Q199 | - |  |  | SI | VA-Nr-UA-OU |
| Q20 | - |  |  | SI | Add-OS-Fx |
| Q200 | - |  |  | SI | VA-Dt |
| Q201 | - |  |  | SI | VA-Nr |
| Q202 | - |  |  | SI | Static Rx |
| Q203 | - |  |  | SI | OD |
| Q204 | - |  |  | SI | OS |
| Q205 | - |  |  | SI | OU |
| Q206 | - |  |  | SI | Cyl |
| Q207 | - |  |  | SI | Axis |
| Q208 | - |  |  | SI | Add |
| Q209 | - |  |  | SI | VA-Dt |
| Q21 | - |  |  | SI | Add-OD-WG |
| Q210 | - |  |  | SI | VA-Nr |
| Q211 | - |  |  | SI | Prescription Rx |
| Q212 | - |  |  | SI | OD |
| Q213 | - |  |  | SI | OS |
| Q214 | - |  |  | SI | OU |
| Q215 | - |  |  | SI | Sph |
| Q216 | - |  |  | SI | Cyl |
| Q217 | - |  |  | SI | Add |
| Q218 | - |  |  | SI | VA-Dt |
| Q219 | - |  |  | SI | VA-Nr |
| Q22 | - |  |  | SI | Add-OS-WG |
| Q23 | - |  |  | SI | Add-OD-UA |
| Q24 | - |  |  | SI | Notes |
| Q25 | - |  |  | SI | Notes |
| Q250 | - |  |  | SI | Light & Accommodation 2 |
| Q256 | - |  |  | SI | Visual Activity - Uncorrected |
| Q257 | - |  |  | SI | VA - Dt |
| Q258 | - |  |  | SI | OU |
| Q259 | - |  |  | SI | Wearing Glasses Rx |
| Q26 | - |  |  | SI | Rx Date |
| Q260 | - |  |  | SI | OD |
| Q261 | - |  |  | SI | OS |
| Q262 | - |  |  | SI | OU |
| Q263 | - |  |  | SI | Sph |
| Q264 | - |  |  | SI | Cyl |
| Q265 | - |  |  | SI | Axis |
| Q266 | - |  |  | SI | Add |
| Q267 | - |  |  | SI | VA - Dt |
| Q268 | - |  |  | SI | VA - Nr |
| Q269 | - |  |  | SI | Dynamic Rx |
| Q27 | - |  |  | SI | VA@Nr-A-Rt |
| Q270 | - |  |  | SI | OD |
| Q271 | - |  |  | SI | OS |
| Q272 | - |  |  | SI | OU |
| Q273 | - |  |  | SI | Sph |
| Q274 | - |  |  | SI | Cyl |
| Q275 | - |  |  | SI | Axis |
| Q276 | - |  |  | SI | Add |
| Q277 | - |  |  | SI | VA - Dt |
| Q278 | - |  |  | SI | VA - Nr |
| Q279 | - |  |  | SI | Static Rx |
| Q28 | - |  |  | SI | VA@Nr-A-Lt |
| Q280 | - |  |  | SI | OD |
| Q281 | - |  |  | SI | OS |
| Q282 | - |  |  | SI | OU |
| Q283 | - |  |  | SI | Sph |
| Q284 | - |  |  | SI | Cyl |
| Q285 | - |  |  | SI | Axis |
| Q286 | - |  |  | SI | Add |
| Q287 | - |  |  | SI | VA - Nr |
| Q288 | - |  |  | SI | Prescription Rx |
| Q289 | - |  |  | SI | OD |
| Q29 | - |  |  | SI | VA-CC@Dt-OD |
| Q290 | - |  |  | SI | OS |
| Q291 | - |  |  | SI | OU |
| Q30 | - |  |  | SI | VA-CC@Dt-OS |
| Q300 | - |  |  | SI | Date |
| Q301 | - |  |  | SI | Time |
| Q302 | - |  |  | SI | Informed Consent? |
| Q303 | - |  |  | SI | Notes |
| Q304 | - |  |  | SI | Notes |
| Q305 | - |  |  | SI | VA-Nr |
| Q306 | - |  |  | SI | VA-Dt |
| Q307 | - |  |  | SI | VA-Nr |
| Q308 | - |  |  | SI | Stereopsis |
| Q309 | - |  |  | SI | Reading |
| Q310 | - |  |  | SI | Colour Vision |
| Q311 | - |  |  | SI | Light & Accommodation |
| Q312 | - |  |  | SI | Reflex - Direct |
| Q313 | - |  |  | SI | Reflex - Consensual |
| Q314 | - |  |  | SI | Reflex - RAPD |
| Q315 | - |  |  | SI | Cover Test & Gaze |
| Q316 | - |  |  | SI | EOM |
| Q317 | - |  |  | SI | OD |
| Q318 | - |  |  | SI | SR: |
| Q319 | - |  |  | SI | IO: |
| Q320 | - |  |  | SI | LR: |
| Q321 | - |  |  | SI | MR: |
| Q322 | - |  |  | SI | IR: |
| Q323 | - |  |  | SI | SO: |
| Q324 | - |  |  | SI | OS |
| Q325 | - |  |  | SI | IO: |
| Q326 | - |  |  | SI | SR: |
| Q327 | - |  |  | SI | MR: |
| Q328 | - |  |  | SI | LR: |
| Q329 | - |  |  | SI | SO: |
| Q33 | - |  |  | SI | VA@Dt-A-Rt |
| Q330 | - |  |  | SI | IR: |
| Q331 | - |  |  | SI | Dry Eye Test |
| Q332 | - |  |  | SI | Schimer's test 1 |
| Q333 | - |  |  | SI | Schimer's test 2 |
| Q334 | - |  |  | SI | IOP-OD (mmHg) |
| Q335 | - |  |  | SI | IOP-OS (mmHg) |
| Q336 | - |  |  | SI | Topical Anesthesia Used |
| Q337 | - |  |  | SI | This chart contains the information from the Refra... |
| Q338 | - |  |  | SI | Completed charts are found at the bottom of the sc... |
| Q339 | - |  |  | SI | Amsler Grid |
| Q34 | - |  |  | SI | VA@Dt-A-Lt |
| Q340 | - |  |  | SI | OD |
| Q341 | - |  |  | SI | OD |
| Q342 | - |  |  | SI | OD |
| Q343 | - |  |  | SI | OS |
| Q344 | - |  |  | SI | OS |
| Q345 | - |  |  | SI | OS |
| Q346 | - |  |  | SI | Prism |
| Q347 | - |  |  | SI | Prism |
| Q348 | - |  |  | SI | Prism |
| Q349 | - |  |  | SI | Prism |
| Q35 | - |  |  | SI | VA-CC@Nr-OU |
| Q350 | - |  |  | SI | Prism |
| Q351 | - |  |  | SI | Prism |
| Q352 | - |  |  | SI | Prism |
| Q353 | - |  |  | SI | Prism |
| Q354 | - |  |  | SI | Prism |
| Q355 | - |  |  | SI | Prism |
| Q356 | - |  |  | SI | Prism |
| Q357 | - |  |  | SI | Prism |
| Q358 | - |  |  | SI | Prism |
| Q359 | - |  |  | SI | Prism |
| Q36 | - |  |  | SI | VA-CC@Dt-OU |
| Q360 | - |  |  | SI | Prism |
| Q361 | - |  |  | SI | Prism |
| Q362 | - |  |  | SI | Base |
| Q363 | - |  |  | SI | Base |
| Q364 | - |  |  | SI | Base |
| Q365 | - |  |  | SI | Base |
| Q366 | - |  |  | SI | Base |
| Q367 | - |  |  | SI | Base |
| Q368 | - |  |  | SI | Base |
| Q369 | - |  |  | SI | Base |
| Q37 | - |  |  | SI | VA-CC@Nr-OD |
| Q370 | - |  |  | SI | Base |
| Q371 | - |  |  | SI | Base |
| Q372 | - |  |  | SI | Base |
| Q373 | - |  |  | SI | Base |
| Q374 | - |  |  | SI | Base |
| Q375 | - |  |  | SI | Base |
| Q376 | - |  |  | SI | Base |
| Q377 | - |  |  | SI | Base |
| Q38 | - |  |  | SI | VA-OU-Dt |
| Q39 | - |  |  | SI | VA-OU-Nr |
| Q40 | - |  |  | SI | VA-CC@Nr-OS |
| Q44 | - |  |  | SI | VA-Nr-ODr |
| Q45 | - |  |  | SI | VA-Dt-A-OU |
| Q46 | - |  |  | SI | VA-Dt-UA-OU |
| Q47 | - |  |  | SI | VA-Nr-A-OU |
| Q48 | - |  |  | SI | VA-Dt-OSr |
| Q49 | - |  |  | SI | VA-Dt-ODr |
| Q50 | - |  |  | SI | VA-Dt-OUr |
| Q54 | - |  |  | SI | VA-Nr-OUr |
| Q60 | - |  |  | SI | Notes |
| Q61 | - |  |  | SI | Notes |
| Q63 | - |  |  | SI | Size@OD |
| Q64 | - |  |  | SI | Direct & Consensual |
| Q66 | - |  |  | SI | Shape@OS |
| Q67 | - |  |  | SI | Size@OS |
| Q68 | - |  |  | SI | Direct & Consensual |
| Q69 | - |  |  | SI | Shape@OD |
| Q71 | - |  |  | SI | Method |
| Q74 | - |  |  | SI | Date |
| Q75 | - |  |  | SI | Time |
| Q76 | - |  |  | SI | Topical Anesthesia used |
| Q77 | - |  |  | SI | Method |
| Q78 | - |  |  | SI | Date |
| Q79 | - |  |  | SI | Time |
| Q82 | - |  |  | SI | OD Lateral Rectus |
| Q83 | - |  |  | SI | OS Lateral Rectus |
| Q84 | - |  |  | SI | OD Medial Rectus |
| Q85 | - |  |  | SI | OD Superior Rectus |
| Q86 | - |  |  | SI | OS Superior Rectus |
| Q87 | - |  |  | SI | OS Medial Rectus |
| Q88 | - |  |  | SI | OD Inferior Rectus |
| Q89 | - |  |  | SI | OS Inferior Rectus |
| Q90 | - |  |  | SI | OD Superior Oblique |
| Q91 | - |  |  | SI | OS Superior Oblique |
| Q92 | - |  |  | SI | OS Inferior Oblique |
| Q97 | - |  |  | SI | Cover test |
| Q98 | - |  |  | SI | Notes |
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