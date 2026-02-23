# web_Msg_OEOrdItem_MultiResolve.FormStrength

**Schema:** web_Msg_OEOrdItem_MultiResolve
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ConversionFactor | double |  |  | SI | Conversion Factor from this UOM to the ordered UOM |
| ID | varchar |  |  | NO | - |
| PHCGenericRtForms | varchar |  |  | SI | - |
| ParRef | varchar |  |  | SI | - |
| PerStrength | double |  |  | SI | Strength Per |
| PerUOMDR | bigint |  | FK | SI | Strength per UOM |
| ReadOnly | bit |  |  | SI | - |
| SelectedStrength | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| Strength | double |  |  | SI | Strength |
| StrengthDR | bigint |  | FK | SI | - |
| UOMDR | bigint |  | FK | SI | Des Ref CTUOM |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*