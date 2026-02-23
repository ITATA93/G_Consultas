# SQLUser.ARC_AdmixtureRec

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCAR_RowId | bigint | PK |  | NO | - |
| ARCAR_Abbreviation | varchar |  |  | SI | Abbreviation |
| ARCAR_AdmixType | varchar |  |  | NO | Admixture Type |
| ARCAR_AllowOrderWOStockCheck | varchar |  |  | SI | Order without Stock |
| ARCAR_AllowToModify | varchar |  |  | SI | Allow to Modify Recipe |
| ARCAR_AllowToOrderAsPCA | varchar |  |  | SI | Allow to Order as PCA |
| ARCAR_AssignedName | varchar |  |  | SI | Assigned Name |
| ARCAR_BaseQty | double |  |  | SI | Base Qty |
| ARCAR_BaseUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| ARCAR_BillSub_DR | varchar |  | FK | SI | Billing Subgroup |
| ARCAR_BulkManuf | varchar |  |  | SI | Bulk Manufacture |
| ARCAR_CTLOC_DR | bigint |  | FK | SI | Main Store |
| ARCAR_Code | varchar |  |  | NO | Admixture Recipe Code |
| ARCAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCAR_ColourCode | varchar |  |  | SI | ColourCode  |
| ARCAR_ColourCodeText | varchar |  |  | SI | ColourCodeText  |
| ARCAR_CreatedDate | date |  |  | SI | CreatedDate |
| ARCAR_CreatedTime | time |  |  | SI | CreatedTime |
| ARCAR_CreatedUserHosp_DR | bigint |  | FK | SI | Des Ref CreatedUserHosp |
| ARCAR_CreatedUser_DR | bigint |  | FK | SI | Des Ref CreatedUser |
| ARCAR_DMDLevel | varchar |  |  | NO | DMDLevel |
| ARCAR_DateFrom | date |  |  | SI | DateFrom |
| ARCAR_DateTo | date |  |  | SI | DateTo |
| ARCAR_DeductPartially | varchar |  |  | SI | Deduct Partially |
| ARCAR_Desc | varchar |  |  | NO | Admixture Recipe Description |
| ARCAR_DoNotUseFinMasVolUnit | varchar |  |  | SI | Do Not Use Final Mass/Volume Unit |
| ARCAR_DrugRegister | varchar |  |  | SI | Drug Register |
| ARCAR_EP_PBSPrescribingRule_DR | bigint |  | FK | SI | Des Ref to PHCPBSPrescribingRule for Extemporaneou... |
| ARCAR_ExpiryDays | integer |  |  | SI | Days to expiry |
| ARCAR_ExpiryHours | integer |  |  | SI | Hours to expiry |
| ARCAR_ExpiryMinutes | integer |  |  | SI | Minutes to Expiry |
| ARCAR_ExpirySource | varchar |  |  | SI | Expiry Source |
| ARCAR_FinalCheckDate | date |  |  | SI | FinalCheckDate |
| ARCAR_FinalCheckTime | time |  |  | SI | FinalCheckTime |
| ARCAR_FinalCheckUser_DR | bigint |  | FK | SI | Des Ref FinalCheckUser |
| ARCAR_FinalForm_DR | bigint |  | FK | SI | Final Form |
| ARCAR_Generic_DR | bigint |  | FK | SI | Generic |
| ARCAR_INCTG_DR | bigint |  | FK | SI | Stock take group |
| ARCAR_ItemCat_DR | bigint |  | FK | SI | Order Subcategory |
| ARCAR_MainItem | varchar |  |  | SI | Main Item |
| ARCAR_ManufInstruction | varchar |  |  | SI | Manufacture Instruction |
| ARCAR_NotSuitableForWardManuf | varchar |  |  | SI | Not Suitable for Ward Manufacture |
| ARCAR_NurseInstructions | varchar |  |  | SI | Nurse Instructions |
| ARCAR_OrderOnItsOwn | varchar |  |  | SI | Order on its own |
| ARCAR_Owner | varchar |  |  | SI | Owner |
| ARCAR_PHCS_DR | bigint |  | FK | SI | Strength |
| ARCAR_PharmCat_DR | bigint |  | FK | SI | Pharmacological Category |
| ARCAR_PharmSubCat_DR | varchar |  | FK | SI | Pharmacological Subcategory |
| ARCAR_PregnancyCat_DR | bigint |  | FK | SI | Pregnancy Category |
| ARCAR_Quantity | double |  |  | SI | Quantity |
| ARCAR_RecAMP_DR | bigint |  | FK | SI | the DMD level recipe created from this recipe (onl... |
| ARCAR_RecVMPP_DR | bigint |  | FK | SI | the DMD level recipe created from this recipe (onl... |
| ARCAR_RecVMP_DR | bigint |  | FK | SI | the DMD level recipe created from this recipe (onl... |
| ARCAR_ReleaseSpecification | varchar |  |  | SI | Release Specification |
| ARCAR_ReorderOnItsOwn | varchar |  |  | SI | Reorder on its own |
| ARCAR_RoundIndivAdmin | varchar |  |  | SI | Round Individual Administration |
| ARCAR_Route_DR | bigint |  | FK | SI | Route |
| ARCAR_SchedDrugClass_DR | bigint |  | FK | SI | Scheduled Drug Classification |
| ARCAR_Solvent_DR | varchar |  | FK | SI | Solvent |
| ARCAR_SubtractAdditive | varchar |  |  | SI | [DEPRECATED]Replaced by Volume Calculator in TrakC... |
| ARCAR_UOM_DR | bigint |  | FK | SI | UOM |
| ARCAR_UpdatedDate | date |  |  | SI | UpdateDate |
| ARCAR_UpdatedTime | time |  |  | SI | UpdateTime |
| ARCAR_UpdatedUserHosp_DR | bigint |  | FK | SI | Des Ref UpdateUserHosp |
| ARCAR_UpdatedUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ChildQ24DR | - |  |  | SI | Child Reference: Otros Artículos Personales |
| Q17Q1 | - |  |  | SI | Sostén |
| Q17Q10 | - |  |  | SI | Otros |
| Q17Q2 | - |  |  | SI | Calzón |
| Q17Q3 | - |  |  | SI | Calzoncillo |
| Q17Q4 | - |  |  | SI | Calcetines |
| Q17Q5 | - |  |  | SI | Polera |
| Q17Q6 | - |  |  | SI | Chaleco |
| Q17Q7 | - |  |  | SI | Pantalón |
| Q17Q8 | - |  |  | SI | Falda |
| Q17Q9 | - |  |  | SI | Chaqueta |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*