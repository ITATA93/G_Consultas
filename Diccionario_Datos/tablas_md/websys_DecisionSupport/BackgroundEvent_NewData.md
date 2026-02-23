# websys_DecisionSupport.BackgroundEvent_NewData

**Schema:** websys_DecisionSupport
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BackgroundEvent | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| NewData | varchar |  |  | SI | NewData |
| element_key | varchar |  |  | NO | NewData array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*