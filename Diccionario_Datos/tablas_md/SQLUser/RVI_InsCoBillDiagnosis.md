# SQLUser.RVI_InsCoBillDiagnosis

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIA_ParRef | bigint | PK |  | NO | RVI_InsCompanyBill Parent Reference |
| DIA_Childsub | double |  |  | NO | Childsub |
| DIA_Depart_DR | varchar |  | FK | SI | Des Ref to NFMI Dep |
| DIA_DischargeCode | varchar |  |  | SI | Discharge Code |
| DIA_InsurDesc | varchar |  |  | SI | Insurance Description |
| DIA_MRCICDx_DR | bigint |  | FK | SI | Des Ref MRCICDx |
| DIA_NoDaysIPPostDischMed | double |  |  | SI | No of Days IP and PostDischarged Med |
| DIA_OperPerformed | varchar |  |  | SI | Operation Performed |
| DIA_Print | varchar |  |  | SI | Print |
| DIA_ReasonInjury | varchar |  |  | SI | Reason for Injury |
| DIA_RowId | varchar |  |  | NO | - |
| DIA_SpecialCode | varchar |  |  | SI | Special Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*